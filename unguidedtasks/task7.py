class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    def display(self):
        current = self.head
        while current.next:
            print(current.data, end=" ")
            current = current.next
        print("None")
    def Sorting(self):
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp and temp.next:
                if temp.data > temp.next.data:
                    temp.data, temp.next.data = temp.next.data, temp.data 
                    swapped = True
                temp = temp.next
link = DoublyLinkedList()
amount = [56,32,76,12,78,87]
for n in amount:
    link.append(n)
link.display()
link.Sorting()
link.display()