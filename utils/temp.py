# utils/temp.py
class TempGen:
    def __init__(self):
        self.counter = 0

    def new(self):
        name = f"%{self.counter}"
        self.counter += 1
        return name
