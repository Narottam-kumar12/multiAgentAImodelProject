# memory.py
class DebateMemory:
    def __init__(self):
        self.transcript = []

    def update_memory(self, argument):
        self.transcript.append(argument)
