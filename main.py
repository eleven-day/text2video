import os
from tts_module import generate_audio
from video_generator import create_video

def main():
    # 输入文本
    input_text = input("请输入要转换为视频的文本: ")

    # 设置 OpenAI API 密钥
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("请设置环境变量 OPENAI_API_KEY 来使用 OpenAI 的服务！")

    # 选择背景类型
    background_type = input("选择背景类型（1: 单张图片, 2: 图片文件夹, 3: 视频）: ")

    if background_type == "1":
        background_path = input("请输入单张图片的路径: ")
    elif background_type == "2":
        background_path = input("请输入图片文件夹路径: ")
    elif background_type == "3":
        background_path = input("请输入背景视频文件路径: ")
    else:
        raise ValueError("无效的背景类型选择！")

    # 调用 TTS 模块生成音频
    audio_path = generate_audio(input_text, openai_api_key)

    # 调用视频生成模块合成视频
    output_video_path = "assets/output/generated_video.mp4"
    create_video(audio_path, background_path, background_type, output_video_path)

    print(f"视频已生成，路径为: {output_video_path}")

if __name__ == "__main__":
    main()