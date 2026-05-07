import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Video Downloader PRO", page_icon="🚀")
st.title("🚀 Ultimate Video Downloader")
st.markdown("YouTube, Instagram, FB - Sab chalega!")

url = st.text_input("Link yahan paste karein:")

if st.button("Download"):
    if url:
        try:
            if os.path.exists("video.mp4"): os.remove("video.mp4")
            
            with st.spinner('YouTube security bypass ho rahi hai...'):
                ydl_opts = {
                    'format': 'best',
                    'cookiefile': 'cookies.txt', # Aapki cookies file
                    'outtmpl': 'video.mp4',
                    'nocheckcertificate': True,
                    'quiet': True,
                    # Yeh naya tareeka hai block todne ka:
                    'extractor_args': {
                        'youtube': {
                            'player_client': ['android', 'ios'],
                            'skip': ['hls', 'dash']
                        }
                    },
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',
                    }],
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video.mp4"):
                    with open("video.mp4", "rb") as f:
                        st.success("Download Ready!")
                        st.download_button("📥 Mobile mein Save Karein", data=f, file_name="video.mp4")
                else:
                    st.error("Server ne file block kar di. Ek baar link badal kar try karein.")
        except Exception as e:
            st.error(f"Error: {e}")
