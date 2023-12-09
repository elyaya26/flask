import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Говорите что-нибудь:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print("Вы сказали: {}".format(text))
except sr.UnknownValueError:
    print("Не удалось распознать речь")
except sr.RequestError as e:
    print("Ошибка при запросе к сервису распознавания речи; {0}".format(e))

from gtts import gTTS
import os

text = "Привет! Как я могу вам помочь?"
tts = gTTS(text=text, lang='ru')
tts.save("output.mp3")
os.system("start output.mp3")  # Для воспроизведения аудио

import pyttsx3

text = "Привет! Как я могу вам помочь?"
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()


from gtts import gTTS
import os

text = "Привет! Как я могу вам помочь?"
tts = gTTS(text=text, lang='ru')
tts.save("output.mp3")
os.system("start output.mp3")

import pyttsx3

text = "Привет! Как я могу вам помочь?"
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

import speech_recognition as sr
from gtts import gTTS
import os

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите что-нибудь:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали: {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
        return None
    except sr.RequestError as e:
        print("Ошибка при запросе к сервису распознавания речи; {0}".format(e))
        return None

def generate_speech(text):
    if text:
        tts = gTTS(text=text, lang='ru')
        tts.save("output.mp3")
        os.system("start output.mp3")

def main():
    input_text = recognize_speech()
    if input_text:
        response_text = "Вы сказали: {}".format(input_text)
        generate_speech(response_text)

if __name__ == "__main__":
    main()

