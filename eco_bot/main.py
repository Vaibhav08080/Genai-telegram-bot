from dotenv import load_dotenv
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import openai

load_dotenv()
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class Reference:
    '''
    Reference class for storing the reference text
    '''
    def __init__(self, text: str = ""):
        self.text = text

reference = Reference()
model_name = "gpt-3.5-turbo"

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()

@dp.message(Command("help"))
async def help_handler(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
Hi There, I'm Telegram bot created by Bappy! Please follow these commands --
/start -- to start the conversation
/clear -- to clear the past conversation and context.
/help -- to get this help menu.
I hope this helps. :)
"""
    await message.answer(help_command)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())