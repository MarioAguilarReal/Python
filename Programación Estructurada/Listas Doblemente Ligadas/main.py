from classes import DoublyLinkedList

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(9)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(3)

print(my_doubly_linked_list)
my_doubly_linked_list.insert(2,12)
print(my_doubly_linked_list)
print(f'Head: {my_doubly_linked_list.head.value}')
print(f'Tail: {my_doubly_linked_list.tail.value}')
print(f'leng: {my_doubly_linked_list.size}')
