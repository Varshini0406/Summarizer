import streamlit as st
from models import your_summarization_model
from utils import your_preprocessing_functions

# Load your trained model (adjust the loading mechanism based on how you saved it)
try:
    model = your_summarization_model.load_model("path/to/your/model")
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

# Function to perform summarization
def summarize_text(text):
    processed_text = your_preprocessing_functions.preprocess(text)
    summary = your_summarization_model.generate_summary(model, processed_text) # Adjust based on your model's API
    return summary

def main():
    st.title("Text Summarization App")

    input_text = st.text_area("Enter text to summarize:", height=300)

    if st.button("Summarize"):
        if input_text:
            with st.spinner("Summarizing..."):
                summary = summarize_text(input_text)
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()