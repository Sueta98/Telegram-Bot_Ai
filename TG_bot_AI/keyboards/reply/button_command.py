from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def gen_reply_markup():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton(text="Выбрать персонажа"),
        KeyboardButton(text="Помощь"),
    )
    return keyboard

