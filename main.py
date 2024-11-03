import asyncio
from random import random
from tkinter.font import names
import random


from aiogram import Bot,Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values


token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

unique_users = set()

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name

    unique_users.add(user_id)

    unique_user_count = len(unique_users)

    msg = (f"Привет, {name}! Р рад видеть тебя здесь. Сейчас бот уже обслуживает {unique_user_count} пользователей. "
           f"Напиши /minfo, чтобы узнать свой ID, или попробуй "
           f"/random, если хочешь получить случайное имя. "
           f"Если нужно повторить любое сообщение, вы можете отправить любое сообщение и добавь текст,"
           f" который хочешь отправить и оно опять вам отправиться. Чем могу помочь?")
    await message.answer(msg)

@dp.message(Command('minfo'))
async def minfo_handler(message: types.Message):
    name = message.from_user.first_name
    user_id = message.from_user.id
    msg = f'ваш айди {name},{user_id}'
    await message.answer(msg)

names = ["алексей","мария","иван","анна","сергей","елена"]
@dp.message(Command('random'))
async def random_names_handler(message: types.Message):
    name = random.choice(names)
    await message.answer(f"вот случайное имя которое вам выпало,хотите ещё раз попробовать?,занова введите команду /random,спасибо вам за игру:):{name}")

@dp.message()
async def unknown_command_handler(message: types.Message):
    if message.text.startswith("/"):
        await message.answer("Извините пока что я не умею отвечать на такие команды попроьбуйте:/random,/start,/minfo")
    else:
        await message.answer(message.text)

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())