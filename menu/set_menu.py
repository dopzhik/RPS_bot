from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon_ru import lexicon_commands_ru

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in lexicon_commands_ru.items()
    ]
    await bot.set_my_commands(main_menu_commands)