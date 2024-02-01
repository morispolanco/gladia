import streamlit as st
import requests

st.title("Audio Transcription App")

audio_file = st.file_uploader("Upload an audio file (m4a format)", type="audio/m4a")

if audio_file is not None:
    headers = {
        'x-gladia-key': '16d52384-d97c-4557-809b-865c2ef2460c',
    }
    files = {
        'audio': audio_file,
    }

    response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)

    if response.status_code == 200:
        st.success("Transcription complete!")
        data = response.json()
        transcript = data['result']['alternatives'][0]['transcript']
        st.write("Transcript:")
        st.write(transcript)
    else:
        st.error("An error occurred during transcription.")
