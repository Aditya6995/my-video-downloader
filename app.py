import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Pro Video Downloader", page_icon="🎥")

st.title("🎥 Ultimate Video Downloader")

url = st.text_input("Video Link Paste Karein:", placeholder="https://www.youtube.com/...")

if st.button("Download Video"):
    if url:
        try:
            with st.spinner('Cookies use karke YouTube se permission le rahe hain...'):
                if os.path.exists("video.mp4"):
                    os.remove("video.mp4")
                
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'video.mp4',
                    'cookiefile': 'cookies.txt',  # Yeh sabse zaroori line hai
                    'noplaylist': True,
                    'quiet': True,
                    'no_warnings': True,
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.success("Download Taiyar Hai!")
                    st.download_button(
                        label="Video Save Karein",
                        data=file,
                        file_name="video.mp4",
                        mime="video/mp4"
                    )
        except Exception as e:
            st.error(f"Dikat: {str(e)}")
    else:
        st.warning("Link toh daaliye!")
