import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'


from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text="Hello, World!")

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# APIを叩いてresponseに入れている
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

filename = "output.mp3"
with open(filename, "wb") as out:
    out.write(response.audio_content)
    print(f"音声データは{filename}ファイルに書き出しました")