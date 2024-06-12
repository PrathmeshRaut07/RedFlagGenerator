from better_profanity import profanity
import re

def censor_text(text):
    # Load the profanity word list (optional step to customize your list)
    profanity.load_censor_words()

    # Split the text into sentences or clauses on periods, commas, or question marks
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|,)\s', text)

    # Check each sentence or clause for profanity and replace if necessary
    censored_sentences = []
    for sentence in sentences:
        print(sentence, profanity.contains_profanity(sentence))
        if profanity.contains_profanity(sentence):
            censored_sentences.append("RED flag")
        else:
            censored_sentences.append(sentence)
    
    # Join the processed sentences back into a single string
    return ' '.join(censored_sentences)

# Example text
text = "Ram was a boy, he troubles a lot in the evening. Ram, he troubles girls a lot too. He pulls girls' clothes, he troubles girls a lot, Ram should be punished, this is the zxqrm set of open API of Shri Ram"

# Censor the text
censored_text = censor_text(text)
print(censored_text)
