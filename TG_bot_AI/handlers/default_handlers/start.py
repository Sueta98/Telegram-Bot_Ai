from telebot.types import Message
from keyboards.reply.button_command import gen_reply_markup
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Привет, {message.from_user.full_name}!",
        reply_markup=gen_reply_markup()  # Передаем клавиатуру здесь
    )
