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
            with st.spinner('Processing...'):
                # Purani file delete karna
                if os.path.exists("video.mp4"):
                    os.remove("video.mp4")
                
                # Nayi settings: Sirf 'best' mangna (FFmpeg ki zaroorat nahi)
                ydl_opts = {
                    'format': 'best', 
                    'outtmpl': 'video.mp4',
                    'noplaylist': True,
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # Download button dikhana
                with open("video.mp4", "rb") as file:
                    st.success("Taiyar hai!")
                    st.download_button(
                        label="Click here to Save Video",
                        data=file,
                        file_name="video.mp4",
                        mime="video/mp4"
                    )
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Pehle link toh daaliye!")
