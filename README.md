# GenAI Telegram Bot

A simple Telegram bot built with [aiogram](https://github.com/aiogram/aiogram) and OpenAI, designed for basic conversation, help commands, and extensibility.

## Features
- `/start` — Start the conversation
- `/help` — Get a help menu with available commands
- `/clear` — (To be implemented) Clear the past conversation and context
- Echoes user messages (example in `echo_bot.py`)
- Easily extensible for OpenAI GPT integration

## Setup

### 1. Clone the repository
```
git clone https://github.com/Vaibhav08080/Genai-telegram-bot.git
cd Genai-telegram-bot/eco_bot
```

### 2. Create and activate a virtual environment (recommended)
```
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate
```

### 3. Install dependencies
```
pip install -r ../requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the `eco_bot` directory with the following content:
```
TELEGRAM_BOT_TOKEN=your-telegram-bot-token-here
OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Run the bot
```
python main.py
```

## File Structure
```
eco_bot/
├── .env            # Environment variables (never commit this!)
├── .gitignore      # Ignore .env and other sensitive files
├── main.py         # Main Telegram bot logic
├── echo_bot.py     # Example echo bot (for reference)
├── README.md       # This file
```

## Notes
- Make sure only one instance of your bot is running at a time, or you will get a `TelegramConflictError`.
- To extend the bot with more commands or OpenAI integration, edit `main.py`.
- Your `.env` file should never be committed to source control.

## License
MIT
