# Nova-AI
Voice-powered AI assistant that listens to your questions, searches answers online, and speaks them in real time.
## Inspiration
The idea for NOVA AI came from the need for a fast, reliable, and voice-powered AI assistant that can provide instant answers to user queries. During the Gemini Live Agent Challenge, I realized the potential of combining voice input, real-time search, and AI-powered response in a single seamless experience.

## What it does
NOVA AI listens to user questions through a microphone, searches for relevant answers using Google via SerpAPI, and provides clear spoken responses in real time. It acts as a lightweight, interactive AI assistant capable of handling live queries efficiently.

## How we built it
The project was built using:
Python for the main application logic
Speech Recognition for capturing microphone input
pyttsx3 for text-to-speech voice output
SerpAPI for real-time Google search results
Modular, loop-based workflow to ensure continuous listening and response

## Challenges we ran into
Ensuring smooth voice output for consecutive answers without interruptions
Handling ambient noise during microphone input
Extracting accurate answers from Google search results when a direct answer box was not available

## Accomplishments that we're proud of
Successfully implemented a real-time voice assistant capable of handling multiple consecutive queries
Integrated live search and speech synthesis for seamless user interaction
Built a shareable, professional AI project in a short hackathon timeframe

## What we learned
How to combine voice recognition, AI search, and TTS in a single Python application
Techniques to manage concurrency and queues in pyttsx3 for uninterrupted voice output
Best practices for handling live user input and search results in a reliable and efficient way

## What's next for Nova AI
Adding a GUI interface for a more interactive experience
Integrating multilingual support, including Bangla and English
Enhancing the system with Gemini-powered reasoning for richer answers
Implementing activation words like “Hey Nova” for a hands-free experience


