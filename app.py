import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Pro Video Downloader", page_icon="🎥")

st.title("🎥 Ultimate Video Downloader")
st.info("Note: Agar 'Forbidden' error aaye, toh 1-2 baar phir se try karein.")

url = st.text_input("Video Link Paste Karein:", placeholder="https://www.youtube.com/...")

if st.button("Download Video"):
    if url:
        try:
            with st.spinner('YouTube se permission le rahe hain...'):
                if os.path.exists("video.mp4"):
                    os.remove("video.mp4")
                
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                    # Ye headers YouTube ko chakma dene ke liye hain
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-us,en;q=0.5',
                        'Sec-Fetch-Mode': 'navigate',
                    },
                    'nocheckcertificate': True,
                    'geo_bypass': True,
                    'quiet': True
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
            st.error("YouTube block kar raha hai. Ek baar phir button dabaiye ya link check karein.")
            st.code(str(e)) # Isse error saaf dikhega
    else:
        st.warning("Link daalna bhool gaye!")
