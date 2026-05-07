import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Ultra Video Downloader", page_icon="🎥")

st.title("🎥 Pro Video Downloader")
st.write("Link daalein aur video download karein:")

url = st.text_input("Paste Link Here:", placeholder="https://www.youtube.com/...")

if st.button("Download Video"):
    if url:
        try:
            with st.spinner('Dhyan rakhein, YouTube ko thoda mana rahe hain...'):
                if os.path.exists("video.mp4"):
                    os.remove("video.mp4")
                
                # Nayi settings jo YouTube ko lagega ki insaan use kar raha hai
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                    'quiet': True,
                    'no_warnings': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'referer': 'https://www.google.com/',
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.success("Mubarak ho! Video taiyar hai.")
                    st.download_button(
                        label="Ab Click karke Save karein",
                        data=file,
                        file_name="video.mp4",
                        mime="video/mp4"
                    )
        except Exception as e:
            st.error(f"Dikat aa gayi: {str(e)}")
    else:
        st.warning("Pehle link toh daalo!")
