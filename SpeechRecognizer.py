#Importa la libreria de reconocimiento de voz de google:
import speech_recognition as sr

import configparser

r = sr.Recognizer()

config = configparser.ConfigParser()
filename = "settings.ini"
config.read(filename)
keys = [
    "audiofile",
    "txtname"
]

audiofile = config.get("AUDIO", "audiofile")
txtname = config.get("TXT", "txtname")

audio_file = sr.AudioFile(audiofile)

with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
result = r.recognize_google(audio)

with open(txtname,mode ="w") as file:
    file.write("Recognized text:")
    file.write("\n")
    file.write(result)
    print("Yuju! La conversion esta lista")
