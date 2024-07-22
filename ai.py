import os 
import pygame
import speech_recognition as sr
from bot_scrapper import *

def speak(text):
    voice = "en-US-AriaNeural"

    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'

    os.system(command)

    pygame.init() 
    pygame.mixer.init()


    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        
    except Exception as e:
        print(e)
        return ""
    return query

# speak("Hello Saksham, I am your virtual assistant. How can i assist you today!")
# query = take_command()
# print(query)

# while True:

#     query = take_command().lower()
#     print('You said: ' + query)

#     if "hello" in query or "hi" in query:
#         speak("hi , how are you")
#     elif "i am fine" in query:
#         speak("I am good, thank you")
#     elif "how are you" in query:
#         speak("I am good, thank you")
#     elif "who are you" in query:
#         speak("I am your virtual assistant. How can i assist you today!")
#     elif "bye" in query:
#         speak("Bye, have a good day!")


click_on_chat_button()
while True:
    query = take_command().lower()
    print('\n You: '+query)
    sendQuery(query)
    isBubbleLoaderVisible()
    response = retriveData()
    speak(response)
