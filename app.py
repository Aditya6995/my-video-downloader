import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Video Downloader", page_icon="🎥")
st.title("🎥 The Final Bypass Downloader")

url = st.text_input("YouTube/Instagram Link:")

if st.button("Download"):
    if url:
        try:
            with st.spinner('YouTube ke security filter ko tod rahe hain...'):
                if os.path.exists("video.mp4"): os.remove("video.mp4")
                
                ydl_opts = {
                    'format': 'best[ext=mp4]/best', # Sirf MP4 format force karein
                    'cookiefile': 'cookies.txt',
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                    'quiet': True,
                    # Sabse important lines block todne ke liye:
                    'nocheckcertificate': True,
                    'geo_bypass': True,
                    'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
                    'user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.success("Mil gaya! Ab save karein.")
                    st.download_button("Save Video", data=file, file_name="video.mp4", mime="video/mp4")
        except Exception as e:
            st.error("YouTube ne phir se block kiya. Ye cloud server ki problem hai.")
            st.info("Try this: Ek bar Instagram ya Twitter link check kijiye. Agar wo chal raha hai, toh code sahi hai.")
    else:
        st.warning("Link missing!")
