class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
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
    def displayBackward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print("None")
link = DLL()
data = [1,2,3,4,5,0]
for n in data:
    link.append(n)
link.displayBackward()