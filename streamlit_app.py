import requests

def transcribe_voice_notes(api_key, audio_url, language_behavior):
    headers = {
        'x-gladia-key': '16d52384-d97c-4557-809b-865c2ef2460c',
    }

    files = {
        'audio_url': (None, audio_url),
        'language_behaviour': (None, language_behavior),
    }

    response = requests.post('https://api.gladia.io/audio/text/audio-transcription/', headers=headers, files=files)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

# Ejemplo de uso
if __name__ == "__main__":
    api_key = '<your api key>'
    audio_url = 'http://files.gladia.io/example/audio-transcription/split_infinity.wav'
    language_behavior = 'automatic multiple languages'

    transcription_result = transcribe_voice_notes(api_key, audio_url, language_behavior)
    print(transcription_result)


