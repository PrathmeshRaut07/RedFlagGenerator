from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import replicate

# Load environment variables from .env
load_dotenv()

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

def Response(query):
    char = ""
    output = replicate.run(
    "mistralai/mixtral-8x7b-instruct-v0.1",
    input={
        "debug": False,
        "top_k": 50,
        "top_p": 1,
        "prompt": query,
        "temperature": 0.7,
#         "system_prompt": """ 
# You are Text analyser who see the text and based on that detects the api key, sexual content or any other inappropriate conversions like someone is scamming or anything like that in response just find any such content is there or not and give the response of Replacing that lines from the Text to word Red Flag.Just give response of full text after replacing red flag nothing else.
# For Example 
# Text: Hello Rahul how are you.I am fine.Rahul you know I bullied an Girl and removed her clothes.Rahul what??Her api is 45tshwkdhdnd
# Response That I need:Hello Rahul how are you.I am fine.Red Flag.Rahul what??.Red Flag
# You can see on above example I such reaplce whole line which was innappropiate (Rahul you know I bullied an Giel and removed he Clothes)
# similary i want to generate Red Flag on my Text.
# Please Give full text as output with the line with which you have change the Red Flag.
# """,
    "system_prompt":"""
Input:
A sequence of sentences. Each sentence should be evaluated for offensive content.

Task:
Identify and flag only those sentences that contain offensive or inappropriate behavior or language, while ensuring that proper nouns or non-offensive content are not mistakenly flagged. Replace the entire sentence containing offensive content with the phrase "Red Flag". If the sentence is not offensive, leave it unchanged. Return the processed text with sentences correctly separated.

Example:
Input: "Ram was a good boy. He pulls girls' clothes, he troubles girls a lot. Ram should be punished for his actions. This is the zxqrm set of open API of Shri Ram."
Output: "Ram was a good boy. Red Flag. Red Flag. This is the zxqrm set of open API of Shri Ram."

Instructions:

Do not replace names or proper nouns with "Red Flag". The flag should replace only the entire sentence if it contains offensive actions or language.
Consider the context and the potential for harm or offensiveness in each sentence.
Maintain the integrity of non-offensive sentences, including names and technical terms.
The goal is to ensure that the output text remains as informative and coherent as possible, even after offensive sentences are replaced.
Considerations:

Ensure accuracy in detecting offensiveness based on language and context.
Avoid over-flagging by maintaining a clear understanding of cultural and contextual sensitivities.
Proper nouns and technical terms should be preserved unless they are part of an offensive statement.
""",
        "max_new_tokens": 1024,
        "min_new_tokens": -1
    }
)
    for item in output:
        char += item
        #print(item, end="")
    return char

