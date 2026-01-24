import random
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8316309357:AAEDRQs31x-Q6hJWGXIxKCmRA3Cv1HxhtAg"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Привет 👋\nНапиши /r — пришлю случайное число от 1 до 10 🎲"
    )

@dp.message_handler(commands=["r"])
async def random_number(message: types.Message):
    number = random.randint(1, 10)
    await message.answer(f"🎲 Случайное число: {number}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
