#Hindi or English - command
#English
#Reply in English
import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==4.0.0rc1

# 1 - Listen : Hindi or English

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")

    except:
        return ""
    
    query = str(query).lower()
    return query

# print(Listen())

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line,'en')
    data = result.text
    print(f"You : {data}.")
    return data

# 3 - Connect

def MicExecution():
    query = Listen()# Data is saved what we speak.
    data = TranslationHinToEng(query)
    return data

# MicExecution()