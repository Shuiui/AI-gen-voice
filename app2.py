import streamlit as st
from moviepy.editor import VideoFileClip, AudioFileClip
from gtts import gTTS
import os

# Function to generate AI voice
def generate_ai_voice(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_file = 'temp_audio.mp3'
    tts.save(audio_file)
    return audio_file

# Function to replace audio in video
def replace_audio_in_video(video_file, audio_file):
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    final_video = video.set_audio(audio)
    
    output_file = 'output_video.mp4'
    final_video.write_videofile(output_file, codec='libx264')
    return output_file

# Streamlit App
st.title("Video Audio Replacement with AI Voice")

uploaded_file = st.file_uploader("Upload a Video File", type=["mp4", "mov", "avi"])

if uploaded_file:
    st.video(uploaded_file)

    text_input = st.text_area("Enter the text to replace the audio with:", "")
    
    if st.button("Replace Audio"):
        if text_input:
            try:
                # Save the uploaded video temporarily
                video_file = 'temp_video.mp4'
                with open(video_file, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Generate AI voice
                audio_file = generate_ai_voice(text_input)

                # Replace audio in video
                output_video = replace_audio_in_video(video_file, audio_file)

                # Provide download link
                st.success("Audio replaced successfully!")
                st.video(output_video)
                with open(output_video, "rb") as f:
                    st.download_button("Download Video", f, file_name="output_video.mp4")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                # Clean up temporary files
                if os.path.exists(video_file):
                    os.remove(video_file)
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                if os.path.exists(output_video):
                    os.remove(output_video)
        else:
            st.warning("Please enter some text to generate audio.")
