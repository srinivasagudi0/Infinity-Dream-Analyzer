import streamlit as st
from analyzer import analyze, last_analysis, personality_summary
from memory.memory import load_memory, clear_memory

st.set_page_config(page_title="Infinity Dream Analyzer", page_icon="✨", layout="wide")

st.title("Infinity Dream Analyzer")
st.write("This tool analyzes your dreams with psychological insight and remembers prior analyses for context.")

# Sidebar: show history and controls
with st.sidebar:
    st.header("Memory & History")
    history = load_memory()
    st.write(f"Entries saved: {len(history)}")
    if history:
        st.markdown("**Recent analyses:**")
        for idx, entry in enumerate(reversed(history[-5:]), 1):
            st.markdown(f"{idx}. {entry[:140]}{'…' if len(entry) > 140 else ''}")
    if st.button("Clear memory", type="secondary"):
        clear_memory()
        st.success("Memory cleared. Reload to refresh.")
        history = []

st.subheader("Describe your dream")
dream_description = st.text_area("Enter a.txt brief description of your dream:", height=180)

col1, col2, col3 = st.columns(3)
with col1:
    analyze_clicked = st.button("Analyze Dream", type="primary")
with col2:
    last_clicked = st.button("What was my last dream?")
with col3:
    personality_clicked = st.button("Character prediction")

if analyze_clicked:
    with st.spinner("Analyzing your dream..."):
        result = analyze(dream_text=dream_description)
    st.markdown("### Analysis")
    st.success(result)
    history = load_memory()
    st.write(f"Memory now has {len(history)} entries.")

if last_clicked:
    st.markdown("### Last dream / analysis")
    st.info(last_analysis())

if personality_clicked:
    with st.spinner("Summarizing personality traits from past dreams..."):
        summary = personality_summary()
    st.markdown("### Character / personality prediction")
    st.success(summary)

# Full history viewer
with st.expander("View full analysis history"):
    history = load_memory()
    if not history:
        st.write("No history yet.")
    else:
        for i, entry in enumerate(reversed(history), 1):
            st.markdown(f"**{i}.** {entry}")

st.caption("Powered by OpenAI. Past analyses are used for consistency, not repetition.")
