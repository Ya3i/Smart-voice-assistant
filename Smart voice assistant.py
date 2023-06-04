import pyttsx3
import wikipedia

while True:
    text = input('Enter the word you want to search for:')
    result = wikipedia.summary(text, sentences=3)
    print(result)
    voice = pyttsx3.init()
    voice.setProperty('rate', 130)
    voice.setProperty('volume', 0.5)
    voice.say(result)
    voice.runAndWait()
