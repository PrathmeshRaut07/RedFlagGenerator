from flask import Flask, request, render_template, redirect, url_for
from moviepy.editor import AudioFileClip, VideoFileClip
import assemblyai as aai
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from assembly_transcriber import assembly
from response import Response
from hindi_speech import transcribe_hindi_audio
from detector import Detect
transcriber=assembly()

# Load environment variables from .env file



app = Flask(__name__)


def split_audio(audio_path, num_splits=10):
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    split_duration = duration / num_splits

    audio_parts = []
    for i in range(num_splits):
        start = i * split_duration
        end = start + split_duration
        subclip = audio_clip.subclip(start, end)
        part_path = f"{audio_path}_part_{i}.wav"
        subclip.write_audiofile(part_path)
        audio_parts.append(part_path)
    
    audio_clip.close()
    return audio_parts

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file and file.filename.endswith('.mp4'):
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)

            video = VideoFileClip(filepath)
            audio = video.audio
            audio_file = filepath.replace('.mp4', '.wav')
            audio.write_audiofile(audio_file)
            video.close()

            audio_clip = AudioFileClip(audio_file)
            if audio_clip.duration > 120:
                audio_parts = split_audio(audio_file)
                transcriptions = []
                for part in audio_parts:
                    text = transcribe_hindi_audio(transcriber,part)
                    transcriptions.append(text)
                    os.remove(part)
                full_transcription = " ".join(transcriptions)
            else:
                full_transcription = transcribe_hindi_audio(transcriber,audio_file)
            #full_transcription='There was a boy named nishant.I study in Enginnering college. Dont tell any one but I bully the girl and black mail them.I am interested in physics.I will share my girlfriends api key 3425162982k'    

            audio_clip.close()
            os.remove(filepath)
            os.remove(audio_file)

            print(full_transcription)
        
            res=Detect(full_transcription)
            full_transcription=Response(full_transcription)
            return render_template('index.html', transcription=res, transcribed_text=full_transcription)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
