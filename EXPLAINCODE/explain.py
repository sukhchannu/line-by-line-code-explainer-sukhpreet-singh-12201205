import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_code(code_content, language):
    """
    Call Gemini API and get line-by-line explanation
    """
    PROMPT_TEMPLATE = f"""
You are an expert programmer and code explainer.
Explain the following {language} code **line by line**.
For each line, output in the following format:

Line: <the code line>
Explanation: <the explanation in simple words>

Code:
{code_content}

Do not use JSON or markdown. Just provide plain text line by line as above.
"""
  
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(PROMPT_TEMPLATE)

    extracted_response = response.text.strip()
    return extracted_response.split("\n\n")  

def main():
    st.set_page_config(page_title="💻 Line-by-Line Code Explainer", layout="wide")
    st.title("💻 Line-by-Line Code Explainer")

    if os.path.exists("code.css"):
        with open("code.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

  
    code_content = st.text_area(
        "📝 Paste your code here:",
        height=300,
        placeholder="Paste your code here...",
    )

    language = st.selectbox("🖥️ Select programming language:", ["C", "C++", "Python", "Java", "JavaScript"])

    if st.button("🚀 Explain Code"):
        if not code_content.strip():
            st.warning("⚠️ Please paste some code before generating explanation.")
        else:
            with st.spinner("Generating explanation... ⏳"):
                explanations = explain_code(code_content, language)
                if explanations:
                    st.success("✅ Code explained successfully!")
                    st.subheader("📖 Line-by-Line Explanation")

                    for item in explanations:

                        if "Explanation:" in item:
                            line_part, expl_part = item.split("Explanation:", 1)
                            line_part = line_part.replace("Line:", "").strip()
                            expl_part = expl_part.strip()

                          
                            st.markdown(f"<div class='code-line'>{line_part}</div>", unsafe_allow_html=True)
                            st.markdown(f"<div class='explanation'>💡 {expl_part}</div>", unsafe_allow_html=True)
                            st.markdown("<br>", unsafe_allow_html=True)
                        else:
                           
                            st.markdown(f"<div class='code-line'>{item}</div>", unsafe_allow_html=True)
                            st.markdown("<br>", unsafe_allow_html=True)
                else:
                    st.error("Failed to generate explanation. Try again!")

if __name__ == "__main__":
    main()
