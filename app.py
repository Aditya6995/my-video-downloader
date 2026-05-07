import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Video Downloader", page_icon="🎥")
st.title("🎥 YouTube Downloader (Cookies Active)")

url = st.text_input("Paste Link Here:")

if st.button("Download"):
    if url:
        try:
            with st.spinner('Downloading...'):
                if os.path.exists("video.mp4"): os.remove("video.mp4")
                
                ydl_opts = {
                    'format': 'best',
                    'cookiefile': 'cookies.txt',  # Yeh file ko dhoondhega
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.success("Download Ready!")
                    st.download_button("Save to Device", data=file, file_name="video.mp4")
        except Exception as e:
            st.error(f"Error: {e}")
