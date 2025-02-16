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
    def delete(self,data):
        current = self.head
        prev = None
        while current.next:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            prev = current
            current = current.next
link = DoublyLinkedList()
amount = [1,2,3,4,0]
for n in amount:
    link.append(n)
link.display()
link.delete(3)
link.display()