import openai
import os

def generate_audio(text, api_key):
    """
    使用 OpenAI 文本到语音服务生成音频文件
    """
    openai.api_key = api_key

    # 调用 OpenAI TTS API
    response = openai.Audio.create(
        model="whisper-1",  # 根据实际支持的 TTS 模型替换
        text=text
    )

    # 保存音频文件
    audio_path = "assets/output/generated_audio.wav"
    with open(audio_path, "wb") as audio_file:
        audio_file.write(response["audio"])

    print(f"音频已生成，路径为: {audio_path}")
    return audio_path