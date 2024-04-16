"""Implement Stack using Queues"""

class Node:
    def __init__(self, data=None, next_=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next_

class Queue:
    def __init__(self):
        self.queue = Node()

    def pushBack(self, val: int) -> None:
        if self.queue.data:
            temp = self.queue
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(val, None, temp)
        else:
            self.queue = Node(val)

    def popFront(self) -> int:
        if self.queue.data:
            item = self.queue.data
            if self.queue.next:
                self.queue = self.queue.next
                self.queue.prev = None
            else:
                self.queue = Node()
            return item
        return -1

    def peekFront(self) -> int:
        if self.queue.data:
            return self.queue.data
        return -1

    def empty(self) -> bool:
        return not self.queue.data

class MyStack:
    def __init__(self):
        self.a = Queue()
        self.b = Queue()

    def push(self, x: int) -> None:
        self.b.pushBack(x)
        while not self.a.empty():
            self.b.pushBack(self.a.popFront())
        self.a, self.b = self.b, self.a

    def pop(self) -> int:
        return self.a.popFront()

    def top(self) -> int:
        return self.a.peekFront()

    def empty(self) -> bool:
        return self.a.empty()
