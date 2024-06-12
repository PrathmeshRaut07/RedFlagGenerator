from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import replicate
load_dotenv()

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")
def Detect(query):
    char = ""
    output = replicate.run(
    "mistralai/mixtral-8x7b-instruct-v0.1",
    input={
        "debug": False,
        "top_k": 50,
        "top_p": 1,
        "prompt": query,
        "temperature": 0.7,
        "system_prompt": """ 
"You are Text analyser who see the text and based on that detects the api key, sexual content or any other inappropriate conversions like someone is scamming or anything like that in response just give whether any such content is there or not and give the response of that line only nothing else strictly. The sentence that you are not understanding leave them
""",
        "max_new_tokens": 1024,
        "min_new_tokens": -1
    }
)
    for item in output:
        char += item
        #print(item, end="")
    return char

