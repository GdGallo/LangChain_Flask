class ShortTermMemory:
    def __init__(self):
        self.context = []

    def add_context(self, text):
        self.context.append(text)

    def get_context(self):
        return " ".join(self.context)
    
    def clear(self):
        self.context = [] 
