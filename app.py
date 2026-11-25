
import streamlit as st

from translator import LANGUAGES, translate_and_transliterate


st.set_page_config(
    page_title="LinguaAI - Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 LinguaAI")
st.subheader("AI-Powered Multilingual Translator")

st.write(
    "Translate text into different languages and view a "
    "Latin-letter representation to help you read the result."
)

st.info(
    "Choose your target language first, enter your text, "
    "and select the language of your original text."
)

# Target language selection
target_language = st.selectbox(
    "1. Which language do you want to translate into?",
    options=list(LANGUAGES.keys()),
    index=None,
    placeholder="Select target language"
)

# Input text
input_text = st.text_area(
    "2. Enter the text you want to translate",
    placeholder="Example: Hello, how are you?",
    height=150
)

# Source language selection
source_language = st.selectbox(
    "3. What language is your original text in?",
    options=list(LANGUAGES.keys()),
    index=0
)

# Translate button
if st.button("Translate Text 🌐", use_container_width=True):

    if target_language is None:
        st.warning("Please choose a target language.")

    elif not input_text.strip():
        st.warning("Please enter some text.")

    elif source_language == target_language:
        st.warning(
            "Your source and target languages are the same. "
            "Please select a different target language."
        )

    else:
        try:
            with st.spinner(
                "Translating... The first request may take longer while the model loads."
            ):
                result = translate_and_transliterate(
                    input_text,
                    source_language,
                    target_language
                )

            st.success("Translation completed!")

            st.markdown("### 📖 Readable Version")
            st.write(result["roman"])

            st.markdown("### 🌐 Native-Script Translation")
            st.write(result["translation"])

            st.caption(
                f"{source_language} → {target_language}"
            )

            download_content = (
                f"LinguaAI Translation\n"
                f"Original text: {input_text}\n"
                f"Source language: {source_language}\n"
                f"Target language: {target_language}\n\n"
                f"Native-script translation:\n"
                f"{result['translation']}\n\n"
                f"Latin-letter representation:\n"
                f"{result['roman']}\n"
            )

            st.download_button(
                label="Download Translation",
                data=download_content,
                file_name="linguaai_translation.txt",
                mime="text/plain",
                use_container_width=True
            )

        except Exception as error:
            st.error(
                "Translation could not be completed. "
                "Check your internet connection and try again."
            )
            st.caption(f"Technical details: {error}")

st.divider()

st.markdown("#### About LinguaAI")
st.write(
    "LinguaAI uses an AI translation model to translate text "
    "between supported languages. Its readable output is a "
    "transliteration or Latin-letter approximation, not necessarily "
    "a phonetic pronunciation guide."
)

st.caption("LinguaAI | Multilingual AI Translation")
