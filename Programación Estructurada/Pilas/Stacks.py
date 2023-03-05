class Node:
    def __init__(self, value):
        self.value = value
        self.down = None

    def __str__(self):
        return str(self.value)
    
class Stack:
    def __init__(self, value):
        node = Node(value)
        self.height =1
        self.top = node
        

    def __len__(self):
        return self.height
    
    def __str__(self):
        if self.height ==0:
            return "No Hay nodos"
        
        else:
            String = "["
            currentNode = self.top

            for i in range(self.height):
                String += str(currentNode)

                if i is not len(self)-1:
                    String += str(", ")
                currentNode = currentNode.down
            String += "]"
            return String
    
    def push(self, value):
        node = Node(value)

        if self.height == 0:
            self.top = node

        else:
            node.down = self.top
            self.top = node

        self.height +=1

        return node
    
    def pop(self):
        if self.height == 0:
            print("No existen nodos para eliminar")
            self.height=0
            return False
        
        else:
            aux = None

            if self.height == 1:
                aux = self.top
                self.top = None

            elif self.height >1:
                aux = self.top
                self.top = aux.down

            self.height -=1
            return aux
    
