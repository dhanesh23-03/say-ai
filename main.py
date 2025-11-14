import os
import speech_recognition as sr
from gtts import gTTS
import openai
from dotenv import load_dotenv

load_dotenv()

# Configure your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def listen_for_command():
    """Listens for a command from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def generate_response(prompt):
    """Generates a response using the OpenAI API."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I'm having trouble thinking right now."

def speak(text):
    """Converts text to speech and plays it."""
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

def main():
    """Main function to run the AI assistant."""
    speak("Hello, I am your real-time AI assistant. How can I help you today?")
    while True:
        command = listen_for_command()
        if command:
            if "exit" in command.lower() or "quit" in command.lower():
                speak("Goodbye!")
                break
            
            response = generate_response(command)
            speak(response)

if __name__ == "__main__":
    main()
