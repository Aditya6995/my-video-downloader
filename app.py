import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Ultra HQ Downloader", layout="centered")

st.title("🎥 Pro Video Downloader (1080p/4K)")
st.write("Best quality download karne ke liye link daalein:")

url = st.text_input("Paste Link Here:")

if st.button("Download High Quality"):
    if url:
        try:
            # File save karne ka rasta (Mac par temporarily save hoga)
            output_path = 'downloads/%(title)s.%(ext)s'
            
            # HQ Settings
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': 'downloaded_video.mp4', # Fixed name for easy access
                'merge_output_format': 'mp4',
            }

            with st.spinner('Downloading in High Quality (isne thoda time lag sakta hai)...'):
                # Purani file delete karna agar maujood hai
                if os.path.exists("downloaded_video.mp4"):
                    os.remove("downloaded_video.mp4")
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # File ready hone ke baad download button dikhana
                with open("downloaded_video.mp4", "rb") as file:
                    st.success("Download Complete! Niche diye button par click karke save karein.")
                    btn = st.download_button(
                        label="Save Video to Mac",
                        data=file,
                        file_name="high_quality_video.mp4",
                        mime="video/mp4"
                    )
                    
        except Exception as e:
            st.error(f"Error: {e}. Agar FFmpeg install nahi hai toh HQ kaam nahi karega.")
    else:
        st.warning("Link paste kariyé!")