import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Page settings
st.set_page_config(page_title="AI Learning Buddy Jhansi", page_icon="🎓")

st.title("🎓 AI Learning Buddy Jhansi")

# User input
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if not topic.strip():
        st.warning("Please enter a topic.")
    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions on {topic} with answers."

        else:
            prompt = topic

        try:
            response = model.generate_content(prompt)

            if hasattr(response, "text"):
                st.success("Generated Successfully!")
                st.write(response.text)
            else:
                st.error("No response received from Gemini.")

        except Exception as e:
            st.error(f"Error: {e}")
