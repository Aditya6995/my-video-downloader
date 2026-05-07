import streamlit as st
import yt_dlp
import os

st.title("🚀 Ultimate Video Downloader (Bypass Mode)")

url = st.text_input("YouTube Link yahan paste karein:")

if st.button("Download"):
    if url:
        try:
            if os.path.exists("video.mp4"): os.remove("video.mp4")
            
            with st.spinner('YouTube security bypass ho rahi hai...'):
                ydl_opts = {
                    'format': 'best',
                    'cookiefile': 'cookies.txt',
                    'outtmpl': 'video.mp4',
                    'nocheckcertificate': True,
                    'quiet': True,
                    # Yeh hai asli jaadu (CWA client use karna)
                    'extractor_args': {
                        'youtube': {
                            'player_client': ['web', 'mweb', 'android'],
                            'player_skip': ['webpage', 'configs']
                        }
                    },
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept': '*/*',
                        'Origin': 'https://www.youtube.com',
                    }
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video.mp4"):
                    with open("video.mp4", "rb") as f:
                        st.success("Download Ho Gaya!")
                        st.download_button("📥 Click to Save", data=f, file_name="video.mp4")
        except Exception as e:
            st.error(f"Error: {e}")
