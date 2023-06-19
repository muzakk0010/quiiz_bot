import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6107637069:AAHLl3ktZ0URalTpXajLZWb83CgRvOHbQy4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(text="1")
async def echo(message: types.Message):
    #1-savol
    await message.answer_poll(
        question="qaysi o'yin taniqli",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )
    await asyncio.sleep(5)

#2-savol
    await message.answer_poll(
        question="qaysi o'yin grafikasi zo'r",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz",
    )
    await asyncio.sleep(5)
#3-savol
    await message.answer_poll(
        question="qaysi o'yin foydali",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )
    await asyncio.sleep(5)


#4-savol
    await message.answer_poll(
        question="bu o'yinlarni qaysi biri vahshiyona",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )
    await asyncio.sleep(5)

    await message.answer_poll(
        question="bu o'yinlarni qaysinisi versalari eng ko'pi",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )


@dp.message_handler(text="2")
async def echo(message: types.Message):
    #1-savol
    await message.answer_poll(
        question="qaysi o'yin taniqli",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )
    await asyncio.sleep(5)

#2-savol
    await message.answer_poll(
        question="qaysi o'yin grafikasi zo'r",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz",
    )
    await asyncio.sleep(5)
#3-savol
    await message.answer_poll(
        question="qaysi o'yin foydali",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )
    await asyncio.sleep(5)


#4-savol
    await message.answer_poll(
        question="bu o'yinlarni qaysi biri vahshiyona",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )
    await asyncio.sleep(5)

    await message.answer_poll(
        question="bu o'yinlarni qaysinisi versalari eng ko'pi",
        options=["minecraft","pubg","cs:go"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)