from api.Ai_api import call_ai_api
from loader import bot
from database.dialogue_context import dialogue_context


@bot.message_handler(content_types=['text'])
def handle_message(message):
    user_id = message.from_user.id
    character = dialogue_context.get_character(user_id)
    if character:
        question = message.text
        response = call_ai_api(character, question, user_id)
        bot.send_message(user_id, response)
    else:
        bot.send_message(user_id, "Сначала выберите персонажа.")
