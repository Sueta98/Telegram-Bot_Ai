from telebot.types import Message
from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(
        message, "Простите но я не знаю такую команду\n" f"Сообщение: {message.text}\nВам нужна помощь?/"
    )
