# Say - A Real-time AI Assistant

This is a real-time AI assistant that can listen to your voice, understand your commands, and respond in a natural voice.

## Features

- **Real-time Interaction:** Speak to the assistant and get a response in real-time.
- **Extensible Tools:** Easily add new tools to extend the assistant's capabilities.
- **AI-Powered:** Powered by large language models to provide intelligent responses.

## Getting Started

### Prerequisites

- Python 3.7+
- `mpg321` for audio playback on Linux. You can install it using:
  ```bash
  sudo apt-get install mpg321
  ```
  For other operating systems, you might need to find an alternative for playing mp3 files from the command line.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dhanesh23-03/say.git
   cd say
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Create a `.env` file by copying the `.env.example` file:
     ```bash
     cp .env.example .env
     ```
   - Open the `.env` file and add your OpenAI API key:
     ```
     OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
     ```

### Running the Assistant

To run the assistant, simply execute the `main.py` file:

```bash
python main.py
```

## How to Use

- The assistant will greet you when it starts.
- Speak your command clearly into the microphone.
- The assistant will process your command and respond.
- To exit the assistant, say "exit" or "quit".

## Adding New Tools

You can add new tools to the assistant by creating new functions in the `tools` directory. Each function should take the necessary arguments and return a string as the result. You can then integrate these tools into the `main.py` file to be called based on the user's command.
