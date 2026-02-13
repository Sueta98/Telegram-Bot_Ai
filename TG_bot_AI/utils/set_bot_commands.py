from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS, CUSTOM_COMMANDS


def set_all_commands(bot):
    all_commands = DEFAULT_COMMANDS + CUSTOM_COMMANDS
    bot.set_my_commands([BotCommand(command=cmd[0], description=cmd[1]) for cmd in all_commands])

