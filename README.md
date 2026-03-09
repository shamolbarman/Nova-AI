# Nova-AI
Voice-powered AI assistant that listens to your questions, searches answers online, and speaks them in real time.
import speech_recognition as sr
import pyttsx3
from serpapi import GoogleSearch

API_KEY = "bfb29c7e9e242ff3a8faa6cbcc985358f52f5cac30267bf0a986b511934af4c5"

# Voice Engine Setup
voice_engine = pyttsx3.init()
voice_engine.setProperty("rate", 160)
voice_engine.setProperty("volume", 1.0)
voices = voice_engine.getProperty("voices")
voice_engine.setProperty("voice", voices[0].id)

def speak(message):
    print("NOVA:", message)
    voice_engine.say(message)
    voice_engine.runAndWait()  # wait until speech finishes
    voice_engine.stop()        # clear queue for next speech

# Speech Recognition
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        try:
            query = recognizer.recognize_google(audio_data)
            print("You said:", query)
            return query
        except:
            speak("Sorry, I didn't catch that.")
            return ""

# Google Search using SerpAPI
def search_google(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    answer = ""

    if "answer_box" in results:
        box = results["answer_box"]
        if "answer" in box:
            answer = box["answer"]
        elif "snippet" in box:
            answer = box["snippet"]

    if answer == "" and "organic_results" in results:
        answer = results["organic_results"][0]["snippet"]

    if answer == "":
        answer = "No clear answer found."

    return answer

# NOVA AI workflow
def run_assistant():
    while True:
        user_question = listen()

        if user_question == "":
            continue

        print("\nNOVA AI")
        print("Searching...\n")

        result = search_google(user_question)

        print("Result:\n", result)
        speak(result)

        print("Done\n")

# Start Assistant
if __name__ == "__main__":
    run_assistant()
