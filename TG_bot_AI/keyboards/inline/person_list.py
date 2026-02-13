from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def gen_inline_markup():
    keyboard = InlineKeyboardMarkup()
    button_texts = [
        "Иисус Христос",
        "Мухаммед",
        "Александр Македонский",
        "Юлий Цезарь",
        "Галилей",
        "Леонардо да Винчи",
        "Наполеон Бонапарт",
        "Альберт Эйнштейн",
        "Махатма Ганди",
        "Нельсон Мандела"
    ]

    for i in range(0, len(button_texts), 2):
        row_buttons = []
        for j in range(2):
            if i + j < len(button_texts):
                row_buttons.append(InlineKeyboardButton(text=button_texts[i + j], callback_data=button_texts[i + j]))
        keyboard.add(*row_buttons)

    return keyboard


