import os
import speech_recognition as sr
from gtts import gTTS
import openai
from dotenv import load_dotenv
from playsound import playsound
import importlib
import inspect
import json
from tools import sample_tools

load_dotenv()

# Configure your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_tools():
    """Loads tools from the tools directory."""
    tools = {}
    for name, func in inspect.getmembers(sample_tools, inspect.isfunction):
        if not name.startswith("_"):
            tools[name] = func
    return tools

def get_tool_descriptions(tools):
    """Gets a description of the available tools for the AI."""
    descriptions = []
    for name, func in tools.items():
        descriptions.append(f"- {name}: {func.__doc__.strip()}")
    return "\n".join(descriptions)

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

def generate_response(prompt, tools):
    """Generates a response using the OpenAI API, potentially using tools."""
    tool_descriptions = get_tool_descriptions(tools)
    system_prompt = f"""You are a helpful assistant with access to the following tools:
{tool_descriptions}

If you need to use a tool, respond with a JSON object with "tool" and "args" keys.
For example: {{"tool": "calculator", "args": "2+2"}}
If you don't need a tool, respond with a natural language message.
"""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        message = response.choices[0].message.content.strip()

        # Check if the response is a tool call
        try:
            tool_call = json.loads(message)
            if "tool" in tool_call and "args" in tool_call:
                tool_name = tool_call["tool"]
                tool_args = tool_call["args"]
                if tool_name in tools:
                    print(f"Using tool: {tool_name} with args: {tool_args}")
                    tool_result = tools[tool_name](tool_args)
                    # Now, generate a response based on the tool's result
                    second_prompt = f"The tool '{tool_name}' returned the following result: {tool_result}. Please formulate a natural language response based on this."
                    second_response = openai.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": second_prompt}
                        ],
                        max_tokens=150
                    )
                    return second_response.choices[0].message.content.strip()
        except (json.JSONDecodeError, TypeError):
            # Not a tool call, so it's a direct response
            return message

    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I'm having trouble thinking right now."


def speak(text):
    """Converts text to speech and plays it."""
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        playsound("response.mp3")
        os.remove("response.mp3")
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

def main():
    """Main function to run the AI assistant."""
    tools = load_tools()
    speak("Hello, I am your real-time AI assistant. How can I help you today?")
    while True:
        command = listen_for_command()
        if command:
            if "exit" in command.lower() or "quit" in command.lower():
                speak("Goodbye!")
                break
            
            response = generate_response(command, tools)
            speak(response)

if __name__ == "__main__":
    main()
