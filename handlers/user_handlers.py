from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import lexicon_ru
from services.services import get_bot_choice, get_winner
from user_bd.user_dict import users
from config_data.config import load_config

admins = load_config().tg_bot.admins_id

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=lexicon_ru['/start'], reply_markup=yes_no_kb)
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'name': message.from_user.first_name,
            'total_games': 0,
            'wins': 0,
            'draw': 0
        }


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=lexicon_ru['/help'], reply_markup=yes_no_kb)

@router.message(Command(commands='admin'))
async def process_help_command(message: Message):
    all_users = (f'игрок: {value['name']} сыграл {value['total_games']} игр' for key, value in users.items())
    if message.from_user.id in admins:
        await message.answer(text='\n'.join(all_users))
    else:
        await message.answer('Вы не админ')


@router.message(F.text == lexicon_ru['yes_button'])
async def process_yes_answer(message: Message):
    users[message.from_user.id]['total_games'] += 1
    await message.answer(text=lexicon_ru['yes'], reply_markup=game_kb)


@router.message(F.text == lexicon_ru['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=lexicon_ru['no'])


@router.message(F.text == lexicon_ru['stat'])
async def process_stat_show(message: Message):
    await message.answer(text=
                         f'<b>Твоя статистика, {users[message.from_user.id]['name']}:</b>\n\n'
                         f'Всего сыграно: {users[message.from_user.id]['total_games']}\n\n'
                         f'Количество побед: {users[message.from_user.id]['wins']}\n\n'
                         f'Победила дружба: {users[message.from_user.id]['draw']}\n\n'
                         f'Чтобы еще раз сыграть разверни клавиатуру снизу ⬇️')


@router.message(F.text.in_([lexicon_ru['rock'],
                            lexicon_ru['paper'],
                            lexicon_ru['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{lexicon_ru["bot_choice"]}'
                              f'- {lexicon_ru[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    if winner == 'user_won':
        users[message.from_user.id]['wins'] += 1
    elif winner == 'nobody_won':
        users[message.from_user.id]['draw'] += 1
    await message.answer(text=lexicon_ru[winner], reply_markup=yes_no_kb)
