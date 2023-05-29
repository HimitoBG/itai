import speech_recognition as sr
from PIL import Image

# set default duration value to 5 seconds
duration = 3

# initialize the recognizer
r = sr.Recognizer()
print("Please talk")
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=duration)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)

imagetext = text + ".png"
print(imagetext)

im = Image.open(f"D:/Uchenie/python/proekt_ai/{imagetext}")

im.show()
im.close()