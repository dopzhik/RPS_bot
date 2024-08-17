from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import lexicon_ru

router = Router()

@router.message()
async def send_answer(message: Message):
    await message.answer(text=lexicon_ru['other_answer'])