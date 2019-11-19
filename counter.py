# counter.py

class Counter:
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1
        
    def clear(self):
        self.count = 0
        
    def get_value(self):
        return self.count


