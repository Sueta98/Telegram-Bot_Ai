import g4f
from database.dialogue_context import dialogue_context


def call_ai_api(character, question, user_id):
    dialogue_context.add_message(user_id, "user", question)

    context_history = dialogue_context.get_context(user_id)
    system_prompt = f"Ты {character}. Отвечай максимально в его стиле и характере. И не выходи из роли"

    messages = [
        {"role": "system", "content": system_prompt}
    ] + context_history

    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=messages
        )

        dialogue_context.add_message(user_id, "assistant", response)
        return response
    except Exception as e:
        print(f"Ошибка GPT4Free: {e}")
        return "Извините, не удалось сгенерировать ответ."
