import streamlit as st
import requests

def transcribe_audio(api_key, audio_file):
    headers = {
        'x-gladia-key': '16d52384-d97c-4557-809b-865c2ef2460c' ,
    }

    files = {
        'audio': audio_file,
        'toggle_diarization': (None, 'true'),
    }

    response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

def main():
    st.title('Transcripción de Audio con Gladia.io')

    # Agregar la clave de la API
    api_key = st.text_input('Ingrese su clave de API de Gladia.io', type='password')

    # Permitir al usuario cargar un archivo de audio
    audio_file = st.file_uploader('Cargar archivo de audio', type=['mp3', 'wav', 'm4a'])

    if st.button('Transcribir'):
        if api_key and audio_file:
            # Realizar la transcripción
            response = transcribe_audio(api_key, audio_file)
            st.write(response)
        else:
            st.error('Por favor, ingrese la clave de la API y cargue un archivo de audio.')

if __name__ == "__main__":
    main()
