import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '...'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Freiherr bot!\nPowered by Sukhenko.")


@dp.message_handler()
async def echo(message: types.Message):
	if message.text == 'Video':
		await bot.send_video(message.chat.id, open('videoplayback.mp4', 'rb'))
	elif message.text == 'Music':
		await bot.send_audio(message.chat.id, open('music1.mp3', 'rb'))
	else:
		await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)