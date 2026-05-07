import streamlit as st
import yt_dlp
import os

st.title("🚀 Multi-Video Downloader")

url = st.text_input("Koi bhi video link paste karein (YouTube/Insta/FB):")

if st.button("Download Now"):
    if url:
        try:
            # Purani file delete karein
            if os.path.exists("video.mp4"): os.remove("video.mp4")
            
            with st.spinner('Processing...'):
                ydl_opts = {
                    'format': 'best',
                    'cookiefile': 'cookies.txt',
                    'outtmpl': 'video.mp4',
                    'nocheckcertificate': True,
                    'quiet': True,
                    'no_warnings': True,
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video.mp4"):
                    with open("video.mp4", "rb") as f:
                        st.success("Download Ready!")
                        st.download_button("📥 Click to Save", data=f, file_name="video.mp4")
                else:
                    st.error("File nahi ban payi. Link check karein.")
        except Exception as e:
            st.error(f"Error: {e}")
