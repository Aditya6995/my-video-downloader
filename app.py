import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Video Downloader", page_icon="📲")
st.title("📲 Simple Video Downloader")

url = st.text_input("Paste Video Link:")

if st.button("Download"):
    if url:
        try:
            if os.path.exists("video.mp4"): os.remove("video.mp4")
            
            with st.spinner('Downloading... Please wait'):
                ydl_opts = {
                    'format': 'best',
                    'cookiefile': 'cookies.txt',
                    'outtmpl': 'video.mp4',
                    'nocheckcertificate': True,
                    # Block todne ke liye simplified settings:
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video.mp4"):
                    with open("video.mp4", "rb") as f:
                        st.success("Download Ho Gaya!")
                        st.download_button("📥 Save to Phone/PC", data=f, file_name="video.mp4")
                else:
                    st.error("File create nahi hui. Link badal kar dekhein.")
        except Exception as e:
            st.error(f"Error: {e}")
