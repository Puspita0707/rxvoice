# RxVoice – Multilingual Prescription Voice Assistant

## Overview

**RxVoice** is an AI-powered speech application that converts spoken medical prescriptions into multilingual voice instructions. The system is designed to improve healthcare accessibility for patients who may have difficulty reading prescriptions due to language barriers or literacy challenges.

The application leverages Automatic Speech Recognition (ASR), Natural Language Processing (NLP), and Text-to-Speech (TTS) technologies to convert doctor speech into understandable audio instructions in the patient's preferred language.

---

## Key Features

* **Speech-to-Text Transcription**
  Uses OpenAI Whisper to convert spoken medical instructions into text.

* **Real-Time Progressive Transcription**
  Displays transcription progressively to simulate real-time speech recognition.

* **Automatic Language Detection**
  Identifies the spoken language of the input audio.

* **Multilingual Translation**
  Translates prescriptions into multiple Indian languages:

  * English
  * Hindi
  * Bengali
  * Tamil

* **Voice Instruction Generation**
  Converts translated text into audio instructions using Text-to-Speech.

* **Downloadable Voice Output**
  Patients can download the generated voice instructions for later reference.

* **Interactive UI**
  Built with Streamlit for an intuitive and easy-to-use interface.

---

## System Architecture

Speech Input (Microphone / Audio Upload)
↓
Whisper Automatic Speech Recognition
↓
Language Detection
↓
Text Transcription
↓
Multilingual Translation
↓
Text-to-Speech Generation
↓
Audio Instructions for Patients

---

## Technologies Used

* **Python**
* **Streamlit**
* **OpenAI Whisper**
* **Google Translate API (googletrans)**
* **gTTS (Google Text-to-Speech)**
* **Streamlit Audio Recorder**

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Puspita0707/rxvoice.git
cd rxvoice
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Demo Workflow

1. Record doctor speech using the microphone or upload an audio file.
2. The system transcribes the speech using Whisper ASR.
3. The transcription is progressively displayed in the UI.
4. The detected language is shown.
5. The prescription is translated into the selected language.
6. A voice instruction is generated and played.
7. The user can download the audio instruction.

---

## Example Input

Doctor Speech:

"Take one tablet after dinner for five days and drink plenty of water. If symptoms persist, consult your doctor again."

Output:

* Transcribed prescription
* Translated instruction
* Generated voice guidance for the patient

---

## Potential Applications

* Healthcare accessibility for illiterate patients
* Multilingual prescription assistance
* Telemedicine support tools
* Voice-based patient instruction systems

---

## Future Improvements

* Real-time streaming speech recognition
* Integration with OCR for handwritten prescriptions
* Support for additional regional languages
* Mobile application integration
* Medical entity extraction from prescriptions

---

## Author

**Puspita Biswas**

GitHub:
https://github.com/Puspita0707

---

## License

This project is intended for educational and research purposes.
