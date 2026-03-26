from .base import BaseMemory

class SimpleMemory(BaseMemory):
    def __init__(self):
        self.history = []

    def add(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def get_context(self):
        conversation = ""
        for msg in self.history:
            conversation += f"{msg['role']}: {msg['content']}\n"
        return conversation 