class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class Queve:
    def __init__(self, value):
        node = Node(value)
        self.length = 1
        self.next = node

    def __len__(self):