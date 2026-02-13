class DialogueContext:
    def __init__(self):
        self.contexts = {}
        self.characters = {}

    def add_message(self, user_id, role, message):
        if user_id not in self.contexts:
            self.contexts[user_id] = []
        self.contexts[user_id].append({"role": role, "content": message})

    def get_context(self, user_id):
        return self.contexts.get(user_id, [])

    def set_character(self, user_id: int, character: str) -> None:
        self.characters[user_id] = character

    def get_character(self, user_id):
        return self.characters.get(user_id)


dialogue_context = DialogueContext()
