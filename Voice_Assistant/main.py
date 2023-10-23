import os, time, playsound, speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text = text, lang = "en") 
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("hey siddhant") # Only works for lowercase text

def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

speak("hi")
get_audio()