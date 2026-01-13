import json
import os
from typing import List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_PATH = os.path.join(BASE_DIR, "persistent_memory.json")


def load_memory() -> List[str]:
    if not os.path.exists(MEMORY_PATH):
        return []

    try:
        with open(MEMORY_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_memory(memory: List[str]) -> None:
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)


def add(entry: str) -> None:
    memory = load_memory()
    memory.append(entry)
    save_memory(memory)


def clear_memory() -> None:
    """Remove all stored entries."""
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)
