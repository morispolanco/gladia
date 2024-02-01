import requests
import streamlit as st

st.title('Transcripción de audio')

uploaded_file = st.file_uploader("Cargar archivo de audio", type=['mp3', 'wav', 'm4a'])

if uploaded_file is not None:
    headers = {
        'x-gladia-key': '16d52384-d97c-4557-809b-865c2ef2460c',
    }

    files = {
        'audio': uploaded_file,
        'toggle_diarization': (None, 'true'),
    }

    response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)

    st.write(response.text)
