import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

from google.cloud import texttospeech
from IPython.display import Audio


# 関数の作成
gender_type = {
    'defalut': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
    'male': texttospeech.SsmlVoiceGender.MALE,
    'female': texttospeech.SsmlVoiceGender.FEMALE,
    'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
}
lang_code = {
    '英語': 'en-US',
    '日本語': 'ja-JP'
}

lang = '日本語'
gender = 'defalut'
text = "こんにちは、私はプログラミング講師のふーくんです"




client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=text)

voice = texttospeech.VoiceSelectionParams(
    language_code=lang_code[lang], ssml_gender=gender_type[gender]
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# APIを叩いてresponseに入れている
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Audio(response.audio_content)
filename = "output.mp3"
with open(filename, "wb") as out:
    out.write(response.audio_content)
    print(f"音声データは{filename}ファイルに書き出しました")