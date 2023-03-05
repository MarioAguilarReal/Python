class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.down = None
    
    def __str__(self):
        return str(self.value)