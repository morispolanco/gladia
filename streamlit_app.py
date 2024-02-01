import streamlit as st
import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "0f17d11299bd4b988050d81317fa37e8"

def transcribe_audio(file):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file)
    return transcript.text

def main():
    st.title("Audio Transcription App")

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/mp3', start_time=0)
        if st.button("Transcribe"):
            st.write("Transcription:")
            transcript = transcribe_audio(uploaded_file)
            st.write(transcript)

if __name__ == "__main__":
    main()
