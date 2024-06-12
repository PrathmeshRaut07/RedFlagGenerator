from deep_translator import GoogleTranslator
def transcribe_hindi_audio(transcriber,audio_path):
    transcript=transcriber.transcribe(audio_path)
    #print(transcript.text)
    english_text = GoogleTranslator(source='hi', target='en').translate(transcript.text)
    #print(english_text)
    return english_text