import assemblyai as aai
from dotenv import load_dotenv
import os
load_dotenv()

def assembly():  
    aai.settings.api_key=os.getenv("ASSEMBLY_API_KEY")
    config=aai.TranscriptionConfig(language_code='hi')
    transcriber=aai.Transcriber(config=config)
    return transcriber
