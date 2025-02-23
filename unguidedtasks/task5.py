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
        
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
size = DLL()
data = [1,2,3,4,5,6,7,8,9,10]
for i in data:
    size.append(i)
print(f"Length of the DLL is : {size.length()}")