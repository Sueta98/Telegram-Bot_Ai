from telebot.types import Message
from loader import bot
from keyboards.inline.person_list import gen_inline_markup
from database.dialogue_context import dialogue_context


@bot.message_handler(func=lambda message: message.text == "Выбрать персонажа")
def start_message(message: Message):
    user_id = message.from_user.id
    dialogue_context.set_character(user_id, None)  # Сброс выбранного персонажа
    bot.send_message(
        message.from_user.id,
        "Выберите собесеника ",
        reply_markup=gen_inline_markup()
    )


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    character = call.data
    bot.send_message(call.from_user.id, f"Вы выбрали {character}. Теперь вы можете задавать ему вопросы.")
    # Установка выбранного персонажа для пользователя
    user_id = call.from_user.id
    dialogue_context.set_character(user_id, character)
    # Удаление inline-кнопок и переход к диалогу
    bot.edit_message_reply_markup(call.message.chat.id, call.message.id)
