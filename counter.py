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

class DecrementingCounter2(Counter):
    """Simple counter that can be incremented, decremented, and cleared."""
    def decrement(self):
        """Decrement counter by 1."""
        self.count -= 1


