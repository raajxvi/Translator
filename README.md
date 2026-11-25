
# 🌍 LinguaAI — AI-Powered Multilingual Translator

LinguaAI is an AI-powered multilingual text translation application built using Python, Streamlit, and Meta's NLLB-200 translation model. It allows users to translate text into different languages and view the translated result in its native script, along with a Latin-letter representation to make unfamiliar scripts easier to read.

## ✨ Features

- 🌐 **Multilingual Translation** — Translate text between supported languages.
- 🎯 **User-Selected Languages** — Choose the source and target languages.
- 🤖 **AI-Powered Translation** — Uses the NLLB-200 multilingual model.
- 📖 **Readable Text Output** — Displays a Latin-letter representation of translated text where supported.
- 📄 **Download Translation** — Save translation results as a text file.
- ⚡ **Cached Model Loading** — Reuses the loaded model to reduce repeated loading overhead.
- 🖥️ **Interactive Interface** — Simple web interface built with Streamlit.

## 🛠️ Tech Stack

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- Meta NLLB-200
- Indic Transliteration
- Unidecode

## 📂 Project Structure

```text
LinguaAI/
├── app.py
├── translator.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version supported by the installed dependencies
- Git
- Internet connection for downloading the translation model

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/LinguaAI.git
cd LinguaAI
```

Replace `YOUR-USERNAME` with your GitHub username and use your actual repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🚀 How to Use

1. Open LinguaAI in your browser.
2. Select the language you want to translate into.
3. Enter the text you want to translate.
4. Select the language of the original text.
5. Click **Translate Text**.
6. View the translated text in its native script.
7. Read the Latin-letter representation where available.
8. Download the translation if required.

## 🧠 How It Works

LinguaAI uses a multilingual sequence-to-sequence neural machine translation model to generate translations.

The application follows this workflow:

```text
User Input
    ↓
Source and Target Language Selection
    ↓
NLLB-200 Translation Model
    ↓
Translated Text
    ↓
Transliteration / Latin-Letter Representation
    ↓
Display and Download Results
```

The translation model generates the translated text. A separate transliteration step converts supported writing systems into Latin letters or provides an approximate representation.

## 🌏 Supported Languages

The current implementation includes English, Tamil, Hindi, Telugu, Malayalam, Kannada, Bengali, Gujarati, Punjabi, Marathi, Urdu, Nepali, French, Spanish, German, Portuguese, Italian, Russian, Arabic, Simplified Chinese, Japanese, Korean, Indonesian, Swahili, and Turkish.

Actual translation quality and language-pair support can vary. The model's documented language codes and capabilities should be checked when adding or modifying languages.

## ⚡ Performance

The first translation can take longer because the model must be downloaded and loaded. LinguaAI caches the model in memory to avoid reloading it during subsequent Streamlit reruns.

Translation speed depends on the processor, available RAM, GPU support, input length, and selected generation settings.

## ⚠️ Limitations

- Translation results may not always be grammatically or contextually perfect.
- Latin-letter output is not guaranteed to represent exact pronunciation.
- Transliteration quality varies across languages and writing systems.
- Running the model on a CPU can be slow.
- An internet connection is generally required for the initial model download.
- The current application processes text; it does not directly translate speech or images.

## 🔮 Future Enhancements

- Automatic source-language detection
- Speech-to-text translation
- Text-to-speech pronunciation
- Translation history
- Improved romanization for additional scripts
- A responsive mobile-friendly interface
- Translation quality evaluation
- Cloud deployment

## 📚 Model Reference

**NLLB-200 Distilled 600M**

https://huggingface.co/facebook/nllb-200-distilled-600M

Review the model card and license before redistributing, deploying, or using the model commercially. NLLB-200 is primarily intended for research and is not intended for production deployment.

## 👩‍💻 Author

Developed as a Python and AI project exploring multilingual communication, neural machine translation, and transliteration.

## 📄 License

The source code and the pretrained model may have different licensing requirements. Add an appropriate license for your own code and comply with the pretrained model's terms.

---

**LinguaAI — Making multilingual communication easier, one translation at a time.**
