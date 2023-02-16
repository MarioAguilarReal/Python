class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.First = None
        self.Size = 0

    def append(self, value):
        myNode = Node(value)
        if self.Size == 0:
            self.First = myNode
            self.Last = myNode
        else:
            currentNode = self.First
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = myNode
            self.Last = myNode
        self.Size +=1

        return myNode

    def remove(self, value):
        if self.Size == 0:
            return False
        else:
            currentNode = self.First
            try:
                while currentNode.next.value != value:
                    currentNode = currentNode.next
                deleteNode = currentNode.next
                currentNode.next = deleteNode.next
                deleteNode.value = None

            except AttributeError:
                return False
        
        self.Size -= 1
        return deleteNode

    def pop(self):
        currentNode = self.First
        i=0
        while i < len(self):
            i+=1
            currentNode = currentNode.next
        if i==0:
            print("No existen Nodos")
        elif i == 1:
            del self.First
            print("Ya no hay Nodos")
            exit()
        else:
            cont = 1
            nodo = self.First
            while cont < len(self)-1:
                nodo = nodo.next
                cont += 1
            self.Last = nodo
            #print(f"{nodo} ____{nodo.next}")
            self.Last.next = None
            self.Size -= 1
    
    def prepend(self, value):
        myNode = Node(value)
        if self.Size == 0:
            self.First = myNode
            self.Last = myNode
            self.Size = 1
        else:
            myNode.next = self.First
            self.First = myNode
            self.Size +=1

    def popfisrt(self):
        if len(self)==0:
            print("No hay nodos")
            return False
        elif len(self)==1:
            emptyNode = Node(" ")
            self.First=emptyNode
            self.Last = emptyNode
            self.Size -= 1
            return 0
        else:
            aux=self.First.next
            self.First=aux
            self.Size -= 1
        
    def get(self, index):
        currentNode = self.First
        if index>self.Size:
            print("Valor no permitido")
        else:
            for i in range(index):
                currentNode = currentNode.next
            return currentNode
    
    def insert (self, index, value):
        myNode = Node(value)
        currentNode = self.First
        if index>self.Size:
            print("Valor no permitido")
        elif index == 0:
            self.First = myNode
            myNode.next=currentNode
            self.Size +=1
        else:
            for i in range(index-1):
                currentNode = currentNode.next
            aux=currentNode.next
            currentNode.next=myNode
            myNode.next=aux
            self.Size+=1

    def set (self, index, value):
        myNode = self.get(index)
        myNode.value=value

    def removeIndex(self, index):
        currentNode = self.First
        if index == len(self):
            self.pop
        else:
            for i in range(index-1):
                currentNode=currentNode.next
                
            deletedNode = currentNode.next
            currentNode.next = deletedNode.next
            deletedNode.value = None
            self.Size-=1
        


    def __len__(self):
        return self.Size

    def __str__(self):
        String = "["
        currentNode = self.First
        for i in range(len(self)):
            String += str(currentNode)
            if i is not len(self)-1:
                String += str(", ")
            currentNode = currentNode.next
        String += "]"
        return String

myList = LinkedList()

