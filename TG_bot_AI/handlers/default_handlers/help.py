from telebot.types import Message
from loader import bot


@bot.message_handler(func=lambda message: message.text == "Помощь")
def bot_help(message: Message):
    help_text = (
        "Если вы столкнулись с ошибкой, перезагрузите бота"
        " или напиши нам на почту: exemple.mail.py"  # Изменить потчу на дейсвительную
    )
    bot.send_message(message.chat.id, help_text)
