from openai import OpenAI
import os
#from dotenv import load_dotenv
from memory.memory import add, load_memory
from key import akey

#load_dotenv()

# Prefer environment variable; fail fast if absent
api_key = akey
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Please configure your API key.")

client = OpenAI(api_key=api_key)


def analyze(dream_text: str) -> str:
    """Analyze a.txt dream using past memory for context and persist the new analysis."""
    if not dream_text or not dream_text.strip():
        return "Please enter a.txt dream description before analyzing."

    memory = load_memory()
    prior = "\n\n".join(memory) if memory else "(no prior analyses yet)"

    system_prompt = (
        "You are a.txt dream analysis assistant.\n"
        "Analyze dreams logically and psychologically.\n"
        "Do not use mysticism or prophecy.\n\n"
        "Past analyses (for context):\n"
        f"{prior}\n\n"
        "Use this context only to be consistent, not repetitive."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": dream_text},
            ],
            temperature=0.7,
            max_tokens=800,
        )
    except Exception as exc:
        return f"Error contacting analysis service: {exc}"

    answer = response.choices[0].message.content.strip()

    # Save combined dream and analysis for future context
    add(f"Dream: {dream_text.strip()}\nAnalysis: {answer}")

    return answer


def last_analysis() -> str:
    """Return the most recent stored analysis (or a.txt friendly fallback)."""
    history = load_memory()
    if not history:
        return "No past analyses found yet."
    return history[-1]


def personality_summary() -> str:
    """Summarize character/personality traits inferred from all stored analyses."""
    history = load_memory()
    if not history:
        return "No past analyses to infer personality yet."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Infer the dreamer's character traits concisely from these past analyses."},
                {"role": "user", "content": "\n\n".join(history)},
            ],
            temperature=0.4,
            max_tokens=300,
        )
    except Exception as exc:
        return f"Error creating personality summary: {exc}"

    return response.choices[0].message.content.strip()
