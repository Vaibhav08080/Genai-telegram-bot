# import logging
# import os
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from dotenv import load_dotenv
# import asyncio

# load_dotenv()

# TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=TELEGRAM_API_TOKEN)
# dp = Dispatcher()

# @dp.message(Command("start"))
# async def start_handler(message: types.Message):
#     await message.answer("atmkbfjapmj")

# @dp.message()
# async def echo_handler(message: types.Message):
#     await message.answer(message.text)

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())