import logging
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

weather_token = "6e8d79779a0c362f14c60a1c7f363e29"
API_TOKEN = '5875493258:AAGXIOEBsWhBgMKx0NYXJsTSQGGdXjptti0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm bot!\nPowered by Anna.")


@dp.message_handler()
async def echo(message: types.Message):
    r1 = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric")
    data = r1.json()
    await message.answer(data)
    city = data["name"]
    temperature = round(data["main"]["temp"])
    humidity = round(data["main"]["humidity"])
    wind = round(data["wind"]["speed"])
    await message.answer(f"***{datetime.datetime.now().strftime('%b %d %Y %H:%M')}***\n"
                                f"Погода в місті: {city}\n\U0001F321Температура: {temperature} C°\n"
                                f"\U0001F4A7Вологість повітря: {humidity} %\n"
                                f"\U0001F32AВітер: {wind} м/с\n ")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)