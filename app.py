import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Video Downloader", page_icon="🎥")
st.title("🎥 Final YouTube Bypass Downloader")

url = st.text_input("YouTube/Instagram Link Paste Karein:")

if st.button("Download"):
    if url:
        try:
            with st.spinner('YouTube se chori-chupe data nikaal rahe hain...'):
                if os.path.exists("video.mp4"): os.remove("video.mp4")
                
                ydl_opts = {
                    'format': 'best',
                    'cookiefile': 'cookies.txt',
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                    'quiet': True,
                    'no_check_certificate': True,
                    'add_header': [
                        'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language: en-us,en;q=0.5',
                        'Sec-Fetch-Mode: navigate',
                    ],
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.success("Success! Ab save kar lijiye.")
                    st.download_button("Save Video", data=file, file_name="video.mp4", mime="video/mp4")
        except Exception as e:
            st.error("YouTube ne server block kar diya hai.")
            st.info("Try this: Ek baar link badal kar kisi doosre video ka link daalein (kabhi-kabhi ek video block hota hai baaki nahi).")
    else:
        st.warning("Pehle link toh daalo!")
