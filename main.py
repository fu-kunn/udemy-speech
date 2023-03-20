import os
import io
import streamlit as st
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

from google.cloud import texttospeech
# from IPython.display import Audio


# 関数の作成
def synthesize_speech(text, lang='日本語', gender='defalut'):
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

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender]
        # language_code=lang_code[lang], ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # APIを叩いてresponseに入れている
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response

st.title('音声出力アプリ')

st.markdown('### データ準備')

input_option = st.selectbox(
    '入力データの選択',
    ('直接入力', 'テキストファイル')
)
input_data = None

if input_option == '直接入力':
    input_data = st.text_area('こちらにテキストを入力してください。', 'Cloud Speech-to-Text用のサンプル文になります。')
else:
    uploaded_file = st.file_uploader('テキストファイルをアップロードして下さい。', ['txt'])
    if uploaded_file is not None:
        content = uploaded_file.read()
        input_data = content.decode()


# lang = '日本語'
# gender = 'defalut'
# text = "こんにちは、私はプロ野球選手のふーくんです"

# """
# 問題：
# genderの引数を変えても声の性別が変わらない
# 日本語➡︎女性
# 英語　➡︎男性
# """


# response = synthesize_speech(text, lang='日本語', gender='male')

# # Audio(response.audio_content)
# filename = "output.mp3"
# with open(filename, "wb") as out:
#     out.write(response.audio_content)
#     print(f"音声データは{filename}ファイルに書き出しました")


