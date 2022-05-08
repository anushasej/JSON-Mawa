class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoubleLL:
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1
    
    def printll(self):
        temp = self.head
        while temp != None:
            print(temp.value,end = " ")
            temp = temp.next

    def append(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.length += 1
        return True
    
    def prepend(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
        self.length += 1
        return True
    
    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def popfirst(self):
        temp = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        temp = self.tail
        for _ in range(self.length -1,index,-1):
            temp = temp.prev
        return temp
    
    def set_value(self,index,value):
        '''
        For changing the node value in LL you can use this function by sending the index 
        position and value to be change
        '''
        if index < 0 or index >= self.length:
            return False
        n = self.get(index)
        n.value = value
        return True

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        newnode = Node(value)
        temp = self.get(index)
        newnode.next = temp
        newnode.prev = temp.prev
        temp.prev.next = newnode
        temp.prev = newnode
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            return self.popfirst()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
  
    
ll = DoubleLL(7)
ll.append(9)
ll.append(10)
ll.prepend(8)
ll.printll()
#print(ll.pop())
#print('\n',ll.popfirst())

print('\n',ll.get(0))
print(ll.set_value(0,22))
ll.insert(0,2)
ll.insert(5,44)
ll.insert(3,55)
ll.printll()
print('\n',ll.length)
print(ll.remove(2))
print(ll.remove(0))
print(ll.remove(4))
ll.printll()
print('\n',ll.length)
