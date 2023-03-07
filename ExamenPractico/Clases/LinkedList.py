from Clases.Node import Node

class DoublyLinkedList:
    def __init__(self):
        #node = Node(value)
        self.size = 0
        self.head = None
        self.tail = None


    def __len__(self):
        return self.size


    def __str__(self):
        String = "["
        currentNode = self.head
        for i in range(len(self)):
            String += str(currentNode)
            if i is not len(self)-1:
                String += str(", ")
            currentNode = currentNode.next
        String += "]"
        return String


    def append(self, value):
        node = Node(value)
        
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
        #currentNode = self.tail
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size +=1
        #print(currentNode, currentNode.next, currentNode.prev, currentNode.next.prev)
        return node
    
    def pop(self):
        currentNode = self.head
        if len(self) == 0:
            print("No existe ningun Nodo")
        elif len(self) == 1:
            self.head = None
            self.tail = None
            self.prev = None
        else:
            aux = self.tail.prev
            self.tail.prev.next = None
            self.tail = aux
            self.size -=1
            #print(self.tail.next)

    def prepend(self, value):
        node = Node(value)
        if len(self) == 0:
            self.head = node
            self.tail = node
            self.size = 1
        else:
            node.next = self.head
            self.head = node
            self.head.next.prev = self.head
            self.size += 1
            actual = self.tail
            #print(actual)
            while actual is not None:
                actual = actual.prev
                #print(actual)

    def remove(self, value):
        currentNode = self.head
        while currentNode.value != value:
            currentNode = currentNode.next
        print(currentNode)
        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev
        self.size -=1

        return currentNode


    def popFirst(self):
        if len(self) ==0:
            print("No hay nodos")
            return False
        elif len(self)==1:
            emptyNode = Node(" ")
            self.head = emptyNode
            self.tail = emptyNode
            self.size -= 1
            return 0
        else:
            aux = self.head.next
            self.head = aux
            self.size -= 1

    def get(self, index):
        currentNode = self.head
        if index>self.size:
            print("Valor no permitido")
        else:
            for i in range(index):
                currentNode = currentNode.next
            return currentNode
        
    def insert(self, index, value):
        myNode = Node(value)
        currentNode = self.head
        if index>self.size:
            print("Valor no permitido")
        elif index == 0:
            self.head = myNode
            myNode.next=currentNode
            currentNode.prev=myNode
            self.size +=1
        else:
            for i in range(index-1):
                currentNode = currentNode.next
            aux = currentNode.next
            currentNode.next=myNode
            myNode.prev=currentNode
            myNode.next = aux
            aux = myNode
            self.size +=1

            print (currentNode)
            #self.Size+=1
    
    def set(self, index, value):
        myNode = self.get(index)
        myNode.value=value
    
    def removeIndex(self, index):
        currentNode = self.head
        if index == len(self):
            self.pop
        else:
            for i in range(index-1):
                currentNode = currentNode.next
            currentNode.prev.next = currentNode.next
            currentNode.next.prev = currentNode.prev
            self.size -=1

        return currentNode
    
    def travelInTheNode(self):
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        return currentNode
    
    
    def check(self):
        #Creo un contador para saber cuantos extremos comparar
        c= float(self.size)
        #Guardo los objetos en variables
        h= self.head
        t=self.tail
        #Creo una variable entera para definir si todos los caracteres se compararon
        #En caso de que sea cierto returna verdadero
        numCond=int(c/2)
        contador=0
        #Ciclo para envaluar los extremos
        for i in range(int(c/2)):
            # print(f" {h} <-> {t}")
            #Si son iguales paso al siguiente
            if(h.value == t.value):
                h = h.next
                t = t.prev
                contador+=1
        if(numCond==contador):
            return print("Si es palindromo")
        else:
            return print("No es palindromo")
    def inString(self, word):
        for i in range (len(word)):
            self.append(word[i])    

