# Infinity Dream Analyzer

Infinity Dream Analyzer is a Streamlit web app that analyzes user-submitted dream descriptions using psychological insights and remembers past analyses for personalized context. It leverages OpenAI's API for analysis and provides features like memory management and personality prediction.

## Features
- Analyze dreams with psychological insights
- Remembers and displays past analyses
- Predicts personality traits from dream history
- Simple, interactive web interface

## Requirements
- Python 3.8+
- streamlit
- openai

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAIAPI_KEY=your_openai_api_key
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## File Structure
- `app.py`: Main Streamlit app
- `analyzer.py`: Dream analysis logic
- `memory/`: Persistent memory management

## License
MIT License

