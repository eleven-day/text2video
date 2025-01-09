import os
import subprocess

def create_video(audio_path, background_path, background_type, output_path):
    """
    根据背景类型和音频合成视频
    """
    # 单张图片作为背景
    if background_type == "1":
        command = [
            'ffmpeg', '-loop', '1', '-i', background_path, '-i', audio_path,
            '-c:v', 'libx264', '-tune', 'stillimage', '-c:a', 'aac', '-b:a', '192k',
            '-pix_fmt', 'yuv420p', '-shortest', output_path
        ]
        
    # 图片文件夹作为背景（生成幻灯片效果）
    elif background_type == "2":
        images = [os.path.join(background_path, img) for img in os.listdir(background_path) if img.endswith((".png", ".jpg", ".jpeg"))]
        images.sort()  # 按文件名排序
        with open("images.txt", "w") as f:
            for img in images:
                f.write(f"file '{img}'\n")
                f.write("duration 1\n")
            f.write(f"file '{images[-1]}'\n")  # Repeat the last image to match the audio duration

        command = [
            'ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'images.txt', '-i', audio_path,
            '-c:v', 'libx264', '-c:a', 'aac', '-b:a', '192k', '-pix_fmt', 'yuv420p', '-shortest', output_path
        ]
    
    # 视频作为背景
    elif background_type == "3":
        command = [
            'ffmpeg', '-i', background_path, '-i', audio_path, '-c:v', 'libx264',
            '-c:a', 'aac', '-b:a', '192k', '-shortest', output_path
        ]
    
    else:
        raise ValueError("无效的背景类型！")

    # 执行ffmpeg命令
    subprocess.run(command, check=True)
    print(f"视频已生成，路径为: {output_path}")