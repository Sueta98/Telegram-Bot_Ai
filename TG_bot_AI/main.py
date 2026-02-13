from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_all_commands

if __name__ == "__main__":
    set_all_commands(bot)
    bot.infinity_polling()

#config.py — здесь объявляются токены, ключи и другие константы;
#states.py — здесь содержатся состояния пользователя;
#api.py — отвечает за взаимодействие с API;
#main.py — здесь создаются обработчики и запускается бот.
