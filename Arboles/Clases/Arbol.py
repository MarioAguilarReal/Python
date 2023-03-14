from Clases.Nodo import Node

class Arbol:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        node = Node(value)
        if self.size == 0:
            self.root = node
            self.size = 1
            print(self.root)
        elif self.size==1:
            aux = self.root
            if node.value == aux.value:
                return False
            elif node.value > aux.value:
                aux.right = node
            else:
                aux.left = node
            self.size +=1
            print(f"izqueirda: {aux.left}")
            print(f"Derecha: {aux.right}")
        else:
            aux = self.root
            while aux.left is not None or aux.right is not None:
                if node.value == aux.value:
                    return False
                elif node.value > aux.value:
                    aux = aux.right
                elif node.value < aux.value:
                    aux = aux.left
            #print(aux)
            if node.value > aux.value:
                aux.right = node
            else:
                aux.left = node
            self.size+=1
            print(f"izquierda {aux.left}")
            print(f"derecha {aux.right}")
    
    def print(self):
        aux = self.root
        self.nder=0
        print(self.root)
        while aux.right is not None and aux.left is not None:
            auxd = aux.right
            auxi = aux.left
            print(auxi, auxd)

            
        
