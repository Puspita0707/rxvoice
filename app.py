from sympy import python
import streamlit as st
import whisper
import tempfile
from googletrans import Translator
from audiorecorder import audiorecorder
from gtts import gTTS
import time

# =========================
# LOAD MODELS
# =========================
model = whisper.load_model("base")
translator = Translator()

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
# AUDIO UPLOAD
# =========================
uploaded_audio = st.file_uploader("Upload Prescription Audio", type=["wav", "mp3"])

# =========================
# MICROPHONE RECORDING
# =========================
st.subheader("Or Record Audio")

# Placeholder for progressive transcription
live_transcript_placeholder = st.empty()

audio = audiorecorder("Start Recording", "Stop Recording")

# =========================
# MICROPHONE PROCESSING
# =========================
if len(audio) > 0:

    st.audio(audio.export().read())

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        audio.export(tmp_file.name, format="wav")
        audio_path = tmp_file.name

    with st.spinner("Transcribing audio..."):
        result = model.transcribe(audio_path)

    transcript = result["text"]
    detected_language = result["language"]

    # =========================
    # PROGRESSIVE TRANSCRIPTION
    # =========================
    words = transcript.split()
    progressive_text = ""

    for word in words:
        progressive_text += word + " "
        live_transcript_placeholder.markdown(
            f"### Live Transcription\n{progressive_text}"
        )
        time.sleep(0.15)

    st.success("Processing Complete ✅")

    st.subheader("Detected Language")
    st.write(detected_language)

    st.subheader("Final Transcription")
    st.write(transcript)

    # =========================
    # TRANSLATION
    # =========================
    target_lang = lang_map[language]

    translated = translator.translate(transcript, dest=target_lang)
    translated_text = translated.text

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
# UPLOADED AUDIO PROCESSING
# =========================
if uploaded_audio is not None:

    if st.button("Generate Voice Instructions"):

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_audio.read())
            audio_path = tmp_file.name

        with st.spinner("Transcribing audio..."):
            result = model.transcribe(audio_path)

        transcript = result["text"]
        detected_language = result["language"]

        # Progressive display
        words = transcript.split()
        progressive_text = ""

        for word in words:
            progressive_text += word + " "
            live_transcript_placeholder.markdown(
                f"### Live Transcription\n{progressive_text}"
            )
            time.sleep(0.15)

        st.success("Processing Complete ✅")

        st.subheader("Detected Language")
        st.write(detected_language)

        st.subheader("Final Transcription")
        st.write(transcript)

        # =========================
        # TRANSLATION
        # =========================
        target_lang = lang_map[language]

        translated = translator.translate(transcript, dest=target_lang)
        translated_text = translated.text

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
