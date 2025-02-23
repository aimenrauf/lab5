class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Browser:
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
    def displayForward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")
    def displayBackward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print("None")
link = Browser()
page = [1,2,3,4,5]
for n in page:
    link.append(n)
link.displayForward()
link.displayBackward()