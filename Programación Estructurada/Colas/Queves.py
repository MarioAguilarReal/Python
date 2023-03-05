class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self, value):
        node = Node(value)
        self.length = 1
        self.first = node

    def __len__(self):
        return self.length
    
    def __str__(self):

        if self.length == 0:
            return "No hay nodos"
        
        else:
            String = "["
            current = self.first

            for i in range(self.length):
                String += str(current)

                if i is not len(self)-1:
                    String += str(", ")
                current = current.next
            String += "]"
            return String
    def enqueue(self, value):

        if self.length == 0:
            self.first = Node(value)
            self.length += 1
        else:
            current = self.first
            while current.next is not None:
                current = current.next
            current.next = Node(value)
            self.length += 1
    def dequeue(self):
        if self.length == 0:
            print("No hay nodos")
        else:
            current = self.first
            self.first = current.next
            self.length -= 1

queue = Queue(2)
print(queue)
queue.enqueue(4)
print(queue)
queue.enqueue(7)
print(queue)
queue.enqueue(12)
print(queue)
queue.enqueue(41)
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)