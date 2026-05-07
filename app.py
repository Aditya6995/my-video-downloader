import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Video Downloader", page_icon="🎥")
st.title("🎥 YouTube Downloader (Final Fix)")

url = st.text_input("Paste Link Here:")

if st.button("Download"):
    if url:
        try:
            with st.spinner('YouTube ko bypass kar rahe hain...'):
                if os.path.exists("video.mp4"): os.remove("video.mp4")
                
                ydl_opts = {
                    'format': 'best',
                    'cookiefile': 'cookies.txt',
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                    'nocheckcertificate': True, # Certificate check skip karein
                    'geo_bypass': True,          # Location block bypass
                    'source_address': '0.0.0.0', # IP handling
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                    }
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.success("Mil gaya! Save kijiye.")
                    st.download_button("Save Video", data=file, file_name="video.mp4")
        except Exception as e:
            st.error(f"Abhi bhi block hai. Error: {e}")
    else:
        st.warning("Link missing hai!")
