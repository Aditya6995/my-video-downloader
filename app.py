import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Pro Video Downloader", page_icon="🎥")

st.title("🎥 Ultimate Video Downloader")

url = st.text_input("Video Link Paste Karein:")

if st.button("Download Video"):
    if url:
        try:
            with st.spinner('Downloading...'):
                ydl_opts = {
                    'format': 'best',
                    'cookiefile': 'cookies.txt',  # Yeh line sahi hai yahan
                    'outtmpl': 'video.mp4',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.download_button("Save Video", data=file, file_name="video.mp4")
        except Exception as e:
            st.error(f"Error: {e}")
