Creating a PoC using streamlit involves a few steps. You'll need to use libraries like moviepy for video processing and a text-to-speech library like gTTS Google Text To Speech for generating audio.
replace_audio Function:
Takes a video file and text as input.
Generates audio using Google Text-to-Speech.
Replaces the audio in the video using MoviePy.
Handles errors and cleans up temporary files.

Streamlit UI:
Provides a file uploader for video files.
A text area for the user to input the desired audio text.
A button to trigger the audio replacement process.
Displays success or error messages as needed.

Save the above code in a file called app2.py. Then, run the following command in your terminal:
streamlit run app2.py
