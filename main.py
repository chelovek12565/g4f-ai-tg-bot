import os
import asyncio
import sys
from dotenv import load_dotenv
from g4f.client import Client
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

load_dotenv()

TOKEN = os.getenv("TOKEN")
dp = Dispatcher()
client = Client()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}! Я - твой ИИ помощник! Задавай мне вопросы и "
                         f"я с радостью на них отвечу!")




