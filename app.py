from sympy import python
import streamlit as st
import whisper
import tempfile
from deep_translator import GoogleTranslator
from gtts import gTTS
import time

# =========================
# LOAD WHISPER MODEL
# =========================
model = whisper.load_model("base")

# =========================
# APP HEADER
# =========================
st.title("RxVoice – Multilingual Prescription Voice Assistant")

st.markdown(
    "### AI-powered system to convert doctor prescriptions into multilingual voice instructions"
)

st.divider()

st.info("Speech → Whisper ASR → Translation → Voice Output")

# =========================
# LANGUAGE SELECTION
# =========================
language = st.selectbox(
    "Choose Patient Language",
    ["English", "Hindi", "Bengali", "Tamil"]
)

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta"
}

# =========================
# AUDIO INPUT (MIC)
# =========================
st.subheader("🎤 Record Doctor Prescription")

audio_bytes = st.audio_input("Record your voice")

# =========================
# AUDIO UPLOAD
# =========================
st.subheader("📂 Or Upload Audio File")

uploaded_audio = st.file_uploader(
    "Upload prescription audio",
    type=["wav", "mp3"]
)

live_transcript_placeholder = st.empty()


def process_audio(audio_data):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio_data)
        audio_path = tmp_file.name

    with st.spinner("Transcribing audio with Whisper..."):
        result = model.transcribe(audio_path)

    transcript = result["text"]
    detected_language = result["language"]

    # Progressive transcription display
    words = transcript.split()
    progressive_text = ""

    for word in words:
        progressive_text += word + " "
        live_transcript_placeholder.markdown(
            f"### Live Transcription\n{progressive_text}"
        )
        time.sleep(0.08)

    st.success("Processing Complete ✅")

    st.subheader("Detected Language")
    st.write(detected_language)

    st.subheader("Final Transcription")
    st.write(transcript)

    # =========================
    # TRANSLATION
    # =========================
    target_lang = lang_map[language]

    translated_text = GoogleTranslator(
        source="auto",
        target=target_lang
    ).translate(transcript)

    st.subheader("Translated Prescription")
    st.write(translated_text)

    # =========================
    # TEXT TO SPEECH
    # =========================
    tts = gTTS(text=translated_text, lang=target_lang)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tts_file:
        tts.save(tts_file.name)

        st.audio(tts_file.name)

        with open(tts_file.name, "rb") as f:
            st.download_button(
                "Download Voice Instruction",
                f,
                file_name="prescription_voice.mp3"
            )


# =========================
# PROCESS MICROPHONE AUDIO
# =========================
if audio_bytes is not None:
    process_audio(audio_bytes.getvalue())


# =========================
# PROCESS UPLOADED AUDIO
# =========================
if uploaded_audio is not None:
    process_audio(uploaded_audio.read())

