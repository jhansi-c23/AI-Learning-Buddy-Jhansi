import streamlit as st
import google.generativeai as genai

# Configure Gemini API from Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page configuration
st.set_page_config(
    page_title="AI Learning Buddy Jhansi",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy Jhansi")
st.write("Learn any topic with AI!")

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

# Generate response
if st.button("Generate"):

    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"""
            Create exactly 5 multiple-choice questions on {topic}.

            Format:
            Question 1
            A)
            B)
            C)
            D)

            Correct Answer:
            Explanation:
            """

        else:
            prompt = topic

        try:
            response = model.generate_content(prompt)
            st.success("Response Generated Successfully!")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")