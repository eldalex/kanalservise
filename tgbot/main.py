import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

load_dotenv(override=True)
bot = Bot(token=os.environ.get('TOKEN'))

dp = Dispatcher(bot)

@dp.message_handler()
async def send_welcome(message: types.Message):
    await message.reply(f"Простите, но я всего лишь пересылаю сообщения.\nI'm sorry, but I'm just forwarding messages.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
