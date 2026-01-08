class ConversationMemory:
    def __init__(self):
        self.context = {}

    def update(self, data: dict):
        self.context.update(data)

    def get(self):
        return self.context