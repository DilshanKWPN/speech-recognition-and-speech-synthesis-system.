import speech_recognition
import pyttsx3

def SpeakNow(command):
    voice=pyttsx3.init()
    voice.say(command)
    voice.runAndWait()


sr = speech_recognition.Recognizer()
with speech_recognition.Microphone()as source2:
    print('silence please')

    sr.adjust_for_ambient_noise(source2, duration=2)
    print('speak now please')

    audio2=sr.listen(source2)

    textt=sr.recognize_google(audio2)
    textt=textt.lower()

    print("Did you say :- " +textt)

    SpeakNow(textt)