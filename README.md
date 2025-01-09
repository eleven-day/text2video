# Text2Video

Text2Video 是一个将文本转换为视频的工具。它使用 OpenAI 的文本到语音服务生成音频，并使用 ffmpeg 将音频和背景合成视频。

## 目录

- [安装](#安装)
- [使用方法](#使用方法)
- [文件结构](#文件结构)
- [示例](#示例)

## 安装

1. 克隆此仓库到本地：
    ```sh
    git clone https://github.com/yourusername/text2video.git
    ```

2. 进入项目目录并安装依赖：
    ```sh
    cd text2video
    pip install -r requirements.txt
    ```

## 使用方法

1. 设置 OpenAI API 密钥：
    ```sh
    export OPENAI_API_KEY='your_openai_api_key'
    ```

2. 运行主程序：
    ```sh
    python main.py
    ```

3. 按照提示输入要转换为视频的文本和背景类型及路径。

## 文件结构

- `main.py`：主程序入口。
- `tts_module.py`：文本到语音模块。
- `video_generator.py`：视频生成模块。
- `requirements.txt`：Python 依赖包列表。
- `assets/`：存放生成的音频和视频文件。

## 示例

运行程序后，按照提示输入以下内容：

- 输入文本：`Hello, this is a test video.`
- 选择背景类型：`1`（单张图片）
- 输入单张图片的路径：`path/to/your/image.jpg`

程序将生成一个包含输入文本音频和背景图片的视频，并保存在 `assets/output/generated_video.mp4`。
