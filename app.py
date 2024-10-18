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
    st.title("🔊文本转语音应用")

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
    output_file = os.path.join(os.getcwd(), file_name)  # 使用当前工作目录

    # 生成按钮
    if st.button("生成音频"):
        with st.spinner("正在生成音频..."):
            # 创建一个事件循环来运行异步函数
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(generate_audio(text, voice, output_file))
        st.success(f"音频文件已保存为: {output_file}")
        st.audio(output_file)

    # 添加侧边栏
    with st.sidebar:
        st.header("💡 关于项目")
        st.write("""
            该项目由视觉AI功能小组基于开源项目进行开发。
            你可以在应用中输入文本，选择声音并生成音频文件。
        """)

        st.header("🔗 相关链接")
        st.markdown("[AI配音流程说明](https://htyf7ss35i.feishu.cn/docx/Ontudw5sHoYKdBxNYF3cqU3jnVc?from=from_copylink)")
        st.markdown("[项目地址](https://github.com/Horan0903/edge-tts)")
        st.markdown("[反馈与建议](https://wj.qq.com/s2/15665410/9cb5/)")

        st.header("📄 使用说明")
        st.write("""
            1. 在文本框中输入要转换的文本。
            2. 从下拉菜单中选择语种和声音。
            3. 输入文件名并选择保存路径。
            4. 点击“生成音频”按钮，生成的音频将会显示在应用中。
        """)


if __name__ == "__main__":
    main()