from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admins_id: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('bot_token'),
            admins_id=list(map(int, env.list('ADMIN_IDS')))
        )
    )
