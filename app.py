import asyncio
import edge_tts
import streamlit as st
import os


# 定义生成音频的异步函数
async def generate_audio(text, voice, output_file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)


# Streamlit应用程序
def main():
    st.title("文本转语音应用")

    # 输入框
    text = st.text_area("输入文本", "这个男人叫小帅，他正躲在屋顶，而他的女友金发妹正在找他")

    # 按语种分类的声音选择
    voice_options = {
        "中文 (Chinese)": {
            "zh-CN-XiaoxiaoNeural": "女声",
            "zh-CN-YunxiNeural": "男声",
            "zh-CN-YunyeNeural": "女声",
            "zh-HK-HiuGaaiNeural": "女声",
            "zh-HK-HiuMaanNeural": "男声",
            "zh-HK-WanLungNeural": "男声",
            "zh-TW-HsiaoChenNeural": "女声",
            "zh-TW-HsiaoYuNeural": "女声",
            "zh-TW-YunJheNeural": "男声"
        },
        "英语 (English)": {
            "en-AU-NatashaNeural": "女声",
            "en-AU-WilliamNeural": "男声",
            "en-CA-ClaraNeural": "女声",
            "en-CA-LiamNeural": "男声",
            "en-GB-LibbyNeural": "女声",
            "en-GB-MaisieNeural": "女声",
            "en-GB-RyanNeural": "男声",
            "en-GB-SoniaNeural": "女声",
            "en-GB-ThomasNeural": "男声",
            "en-US-AriaNeural": "女声",
            "en-US-AvaNeural": "女声",
            "en-US-BrianNeural": "男声",
            "en-US-ChristopherNeural": "男声",
            "en-US-EmmaNeural": "女声",
            "en-US-EricNeural": "男声",
            "en-US-GuyNeural": "男声",
            "en-US-JennyNeural": "女声",
            "en-US-MichelleNeural": "女声",
            "en-US-RogerNeural": "男声",
            "en-US-SteffanNeural": "男声"
        },
        "法语 (French)": {
            "fr-BE-CharlineNeural": "女声",
            "fr-BE-GerardNeural": "男声",
            "fr-CA-AntoineNeural": "男声",
            "fr-CA-SylvieNeural": "女声",
            "fr-CH-ArianeNeural": "女声",
            "fr-CH-FabriceNeural": "男声",
            "fr-FR-DeniseNeural": "女声",
            "fr-FR-HenriNeural": "男声"
        },
        "德语 (German)": {
            "de-AT-IngridNeural": "女声",
            "de-AT-JonasNeural": "男声",
            "de-CH-JanNeural": "男声",
            "de-CH-LeniNeural": "女声",
            "de-DE-AmalaNeural": "女声",
            "de-DE-ConradNeural": "男声",
            "de-DE-KatjaNeural": "女声",
            "de-DE-KillianNeural": "男声"
        }
    }

    # 选择语种和声音
    language = st.selectbox("选择语种", list(voice_options.keys()))
    voice = st.selectbox("选择声音", list(voice_options[language].keys()))

    # 显示性别信息
    st.write(f"所选声音为: {voice_options[language][voice]}")

    # 文件路径输入
    file_name = st.text_input("文件名", "test.mp3")
    output_file = st.text_input("选择保存路径", os.path.join(os.getcwd(), file_name))

    # 生成按钮
    if st.button("生成音频"):
        with st.spinner("正在生成音频..."):
            asyncio.run(generate_audio(text, voice, output_file))
        st.success(f"音频文件已保存为: {output_file}")
        st.audio(output_file)


if __name__ == "__main__":
    main()
