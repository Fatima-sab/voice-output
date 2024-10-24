limport streamlit as st
from gtts import gTTS
import os

# Title of the app
st.title("Text to Speech Converter")

# Text input from the user
user_input = st.text_input("hello google:")

# Button to convert text to audio
if st.button("Convert to Audio"):
    if user_input:
        # Create audio from text
        tts = gTTS(text=user_input, lang='en')
        audio_file = "output.mp3"
        tts.save(audio_file)

        # Provide a download link for the audio file
        st.audio(audio_file, format="audio/mp3")
    else:
        st.warning("Please enter some text before converting.")
