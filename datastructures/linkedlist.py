class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self, list=None):
        self.__head = None
        self.__tail = None
        self.__size = 0

        if list is not None:
            head = False
            prev = None
            for item in list:
                current = Node(item)
                if not head:
                    self.__head = current
                    head = True
                if prev is not None:
                    prev.next = current
                prev = current
            self.__tail = prev
            self.__size = len(list)

    def __repr__(self):
        res = []
        node = self.__head
        while node:
            res.append(node.data)
            node = node.next
        return res

    def __len__(self):
        return self.__size

    #Add a node at the front
    def push(self, data):
        node = Node(data)
        node.next = self.__head
        if self.__head is None:
            self.__tail = node
        self.__head = node
        self.__size += 1
    
    def insert_after(self, node, data):
        if node is None:
            raise RuntimeError("Given node is not defined")

        new_node = Node(data)
        new_node.next = node.next
        if node.next is None:
            self.__tail = new_node
        node.next = new_node
        self.__size += 1

    def insert_index(self, pos, data):
        node = self.find_index(pos)
        new_node = Node(data)
        new_node.next = node.next
        if node.next is None:
            self.__tail = new_node
        node.next = new_node

    #Add a node at the end
    def append(self, data):
        new_node = Node(data)
        self.__size += 1
        self.__tail = new_node

        if self.__head is None:
            self.__head = new_node
            return

        node = self.__head
        while node.next:
            node = node.next
        node.next = new_node

    def fast_append(self, data):
        new_node = Node(data)
        self.__size += 1

        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            return

        self.__tail.next = new_node
        self.__tail = new_node

    def peek(self):
        if self.__head is None:
            return None
        return self.__head.data

    def peek_last(self):
        if self.__tail is None:
            return None
        return self.__tail.data

    def peek_index(self, pos):
        node = self.find_index(pos)
        return node.data

    def remove_first(self):
        if self.__head is None:
            raise RuntimeError("There is no element in linked list to delete")
        
        data = self.__head.data
        if self.__head.next is None:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next

        self.__size -= 1
        return data

    def remove_last(self):
        if self.__tail is None:
            raise RuntimeError("There is no element in linked list to delete")
        
        if self.__tail == self.__head:
            return self.remove_first()
        
        data = self.__tail.data
        node = self.__head
        while node.next != self.__tail:
            node = node.next
        node.next = None
        self.__tail = node.next

        self.__size -= 1
        return data

    def remove(self, key):
        node = self.find(key)
        if node is None:
            raise RuntimeError("There is no such element to remove")
        if node == self.__head:
            return self.remove_first()
        if node == self.__tail:
            return self.remove_last()

        self.__size -= 1
        tmp = self.__head
        while tmp.next != node:
            tmp = tmp.next
        
        data = node.data
        tmp.next = node.next
        return data
    
    def remove_index(self, pos):
        if pos == 0:
            return self.remove_first()
        if pos == self.__size - 1:
            return self.remove_last()
       
        node = self.find_index(pos)

        data = node.next.data
        node.next = node.next.next
        return data

    def find(self, key):
        node = self.__head
        while node is not None and node.data != key:
            node = node.next
        return node

    def find_index(self, pos):
        if pos >= self.__size:
            raise ValueError("Given index out of range")

        node = self.__head
        for i in range(pos):
            node = node.next
        return node

    def distance(self, start, end):
        res = 1
        while start.next != end and start.next != None:
            res += 1
            start = start.next
        
        if start.next == None:
            raise RuntimeError("Given started node does not reach the end node")

        return res

    #It can be implemented also using the size variable
    #Floyd slow and fast pointers approach
    #returns number of nodes in a loop if has one else return None
    def has_loop(self):
        if self.__head is None:
            return False

        slow = self.__head
        fast = self.__head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.distance(slow, fast)
        return None

    def reverse(self):
        prev = None
        current = self.__head
        next = None

        self.__head, self.__tail = self.__tail, self.__head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

    def __iter__(self):
        return LinkedListIterator(self)

    def __del__(self):
        node = self.__head
        while node:
            tmp = node.next
            del node.data
            node = tmp

class LinkedListIterator:
    def __init__(self, linkedlist):
        self._linkedlist = linkedlist
        self._index = linkedlist.peek()

    def __next__(self):
        if self._index is None:
            raise StopIteration
        
        data = self._index
        self._index = self._index.next
        return data

