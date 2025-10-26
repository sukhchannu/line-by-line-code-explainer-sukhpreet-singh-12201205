# line-by-line-code-explainer-sukhpreet-singh-12201205
Line by Line Code Explainer is an AI-powered tool that allows users to paste any piece of code and get a line-by-line explanation of what each line does.


## Project Overview
Paste code, understand it instantly, and learn programming faster.


## Problem Statement
Beginners and even intermediate programmers often struggle to understand unfamiliar code quickly.
Manually analyzing each line is time-consuming, and tutorials or documentation may not explain the logic clearly.


## Solution Summary
I built line-by-line-code-explainer, a AI web app that lets users paste code snippets and receive line-by-line explanations.
It uses Google Gemini API to generate plain-language explanations for each line, helping learners understand logic instantly.


## Tech Stack
Backend: Python, Streamlit
Frontend: Streamlit (built-in UI), HTML + CSS
AI / LLM Models: Google Gemini (gemini-2.0-flash)
Deployment / Hosting: Streamlit Cloud, Render, or Vercel
Version Control: Git + GitHub


## Project Structure
EXPLAINCODE

  - explain.py                              # Main Streamlit app
  - code.css                                # Custom CSS for styling
  - requirements.txt                        # Python dependencies
  - .env                                    # GEMINI_API_KEY
  - exp_env/                                # Python virtual environment
  - README.md                               # Project overview and instructions


## Setup Instructions (with Python)
Follow these exact steps to run your project locally

1. Create and activate a virtual environment:
    python -m venv exp_env
    exp_env\Scripts\activate

2. Install dependencies 
   pip install -r requirements.txt

3. Set Up Environment Variables
    GEMINI_API_KEY=google_gemini_api_key

4. Run the Streamlit application
    streamlit run explain.py

   
## Deployment
Run the app locally:
Activate virtual environment: exp_env\Scripts\activate
Install dependencies: pip install -r requirements.txt
Run the app: streamlit run explain.py
Open the app in your browser (Streamlit will provide a local URL)


## Demo Video 

## Features
  - End-to-end working web app (accessible via browser)
  - Implements AI / LLM-based logic to explain code line by line
  - Clean, responsive UI with easy copy/download of explanations
  - Real-world applicability for students, junior developers, and learners


## Technical Architecture
The system allows users to paste code snippets, sends them to Google Gemini API for line-by-line explanations, and displays the results.

ASCII Diagram:
Frontend (Streamlit UI) -> User pastes code snippet -> Backend (Streamlit + Python) -> AI Model (Google Gemini) -> Generates line-by-line explanations -> Backend sends explanations -> Frontend displays code alongside explanations


##  References
Streamlit Official Documentation
Google Generative AI API Documentation
Tutorials on Python + Streamlit + AI integration

## License 
This project is licensed under the MIT License.


## Acknowledgements
Google for providing Gemini AI models
Streamlit community for excellent UI framework
Online tutorials and forums for fullstack Python guidance





