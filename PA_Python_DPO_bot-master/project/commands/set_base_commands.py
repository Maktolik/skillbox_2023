from telebot.types import BotCommand
from telebot import TeleBot

from config_data.config import BASE_COMMANDS
from logs.loggers import func_logger


@func_logger
def set_base_commands(bot: TeleBot) -> None:
    """
    Устанавливает команды для бота

    params:
    :bot: бот
    """
    bot.set_my_commands(
        [BotCommand(*_) for _ in BASE_COMMANDS]
    )
