import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
from google import genai
from google.genai import types
from serpapi import GoogleSearch

GEMINI_API_KEY = "My_GEMINI_API_KEY_HERE" 
SERP_API_KEY = "My_SERP_API_KEY" 

client = genai.Client(api_key=GEMINI_API_KEY)

class NovaAgent:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 185)
        self.memory = []

    def speak(self, text):
        print(f"NOVA >> {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("\n[NOVA is Listening...]")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"USER >> {query}")
            return query.lower()
        except:
            return ""

    def analyze_vision(self, img_path):
        try:
            with open(img_path, "rb") as f:
                image_data = f.read()
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=["Describe this image in detail for a blind person.", 
                          types.Part.from_bytes(data=image_data, mime_type="image/jpeg")]
            )
            return response.text
        except Exception as e:
            return f"Vision Error: {str(e)}"

    def get_web_data(self, query):
        params = {"engine": "google", "q": query, "api_key": SERP_API_KEY}
        try:
            search = GoogleSearch(params)
            res = search.get_dict()
            return res.get("answer_box", {}).get("snippet") or res["organic_results"][0]["snippet"]
        except:
            return None

    def brain_processing(self, user_input):
        try:
            context = "\n".join(self.memory[-4:])
            full_prompt = f"System: You are Nova, a helpful AI Agent.\nContext:\n{context}\nUser: {user_input}"
            response = client.models.generate_content(model="gemini-2.0-flash", contents=full_prompt)
            self.memory.append(f"User: {user_input}")
            self.memory.append(f"Nova: {response.text}")
            return response.text
        except:
            return None

    def start_agent(self):
        self.speak("Nova Advanced System Initiated. All modules are online.")
        while True:
            query = self.listen()
            if not query: continue
            if any(word in query for word in ["stop", "exit", "offline"]):
                self.speak("Terminating sessions. System offline. Goodbye.")
                break
            elif "open youtube" in query:
                self.speak("Opening YouTube interface.")
                webbrowser.open("https://youtube.com")
            elif "analyze image" in query or "see this" in query:
                self.speak("Please ensure 'test.jpg' is in the project folder. Scanning...")
                if os.path.exists("test.jpg"):
                    description = self.analyze_vision("test.jpg")
                    self.speak(description)
                else:
                    self.speak("Image file not found.")
            else:
                answer = self.brain_processing(query)
                if answer:
                    self.speak(answer)
                else:
                    self.speak("Accessing real-time web databases...")
                    web_res = self.get_web_data(query)
                    self.speak(web_res if web_res else "Data retrieval failed.")

if __name__ == "__main__":
    nova = NovaAgent()
    nova.start_agent()
