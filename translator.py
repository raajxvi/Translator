
import streamlit as st
import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from unidecode import unidecode


MODEL_NAME = "facebook/nllb-200-distilled-600M"


LANGUAGES = {
    "English": "eng_Latn",
    "Tamil": "tam_Taml",
    "Hindi": "hin_Deva",
    "Telugu": "tel_Telu",
    "Malayalam": "mal_Mlym",
    "Kannada": "kan_Knda",
    "Bengali": "ben_Beng",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
    "Marathi": "mar_Deva",
    "Urdu": "urd_Arab",
    "Nepali": "npi_Deva",
    "French": "fra_Latn",
    "Spanish": "spa_Latn",
    "German": "deu_Latn",
    "Portuguese": "por_Latn",
    "Italian": "ita_Latn",
    "Russian": "rus_Cyrl",
    "Arabic": "arb_Arab",
    "Chinese (Simplified)": "zho_Hans",
    "Japanese": "jpn_Jpan",
    "Korean": "kor_Hang",
    "Indonesian": "ind_Latn",
    "Swahili": "swh_Latn",
    "Turkish": "tur_Latn",
}


INDIC_SCRIPTS = {
    "Tamil": sanscript.TAMIL,
    "Hindi": sanscript.DEVANAGARI,
    "Telugu": sanscript.TELUGU,
    "Malayalam": sanscript.MALAYALAM,
    "Kannada": sanscript.KANNADA,
    "Bengali": sanscript.BENGALI,
    "Gujarati": sanscript.GUJARATI,
    "Punjabi": sanscript.GURMUKHI,
    "Marathi": sanscript.DEVANAGARI,
    "Nepali": sanscript.DEVANAGARI,
}


# Cache the model so it is not loaded again on every click.
@st.cache_resource(show_spinner="Loading translation model...")
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Limit CPU threads to avoid excessive thread overhead.
    if device == "cpu":
        torch.set_num_threads(
            max(1, min(4, torch.get_num_threads()))
        )

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    model.to(device)
    model.eval()

    return tokenizer, model, device


def translate_text(text, source_language, target_language):
    if source_language not in LANGUAGES:
        raise ValueError("Unsupported source language.")

    if target_language not in LANGUAGES:
        raise ValueError("Unsupported target language.")

    if not text or not text.strip():
        raise ValueError("Please enter text to translate.")

    tokenizer, model, device = load_model()

    tokenizer.src_lang = LANGUAGES[source_language]

    inputs = tokenizer(
        text.strip(),
        return_tensors="pt",
        truncation=True,
        max_length=256
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    target_token_id = tokenizer.convert_tokens_to_ids(
        LANGUAGES[target_language]
    )

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            forced_bos_token_id=target_token_id,
            max_new_tokens=128,
            num_beams=1,
            do_sample=False
        )

    return tokenizer.batch_decode(
        output,
        skip_special_tokens=True
    )[0]


def transliterate_to_english(text, target_language):
    if not text:
        return ""

    if target_language in INDIC_SCRIPTS:
        try:
            return transliterate(
                text,
                INDIC_SCRIPTS[target_language],
                sanscript.IAST
            )
        except Exception:
            return unidecode(text)

    latin_script_languages = {
        "English", "French", "Spanish", "German",
        "Portuguese", "Italian", "Indonesian",
        "Swahili", "Turkish"
    }

    if target_language in latin_script_languages:
        return text

    # Approximation for scripts without a dedicated transliterator.
    return unidecode(text)


def translate_and_transliterate(
    text,
    source_language,
    target_language
):
    translated_text = translate_text(
        text,
        source_language,
        target_language
    )

    roman_text = transliterate_to_english(
        translated_text,
        target_language
    )

    return {
        "translation": translated_text,
        "roman": roman_text,
        "source_language": source_language,
        "target_language": target_language
    }
