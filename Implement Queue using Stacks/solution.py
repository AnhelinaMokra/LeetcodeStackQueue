"""Implement Queue using Stacks"""
class Node:
    def __init__(self, data=None, next_=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next_

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val: int) -> None:
        if not self.top:
            self.top = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.top
            self.top = new_node

    def pop(self) -> int:
        if self.top:
            val = self.top.data
            self.top = self.top.next
            return val
        return -1

    def peek(self) -> int:
        if self.top:
            return self.top.data
        return -1

    def empty(self) -> bool:
        return not self.top

class MyQueue:
    def __init__(self):
        self.a = Stack()
        self.b = Stack()

    def push(self, x: int) -> None:
        self.a.push(x)

    def pop(self) -> int:
        if self.b.empty():
            while not self.a.empty():
                self.b.push(self.a.pop())
        return self.b.pop()

    def peek(self) -> int:
        if self.b.empty():
            while not self.a.empty():
                self.b.push(self.a.pop())
        return self.b.peek()

    def empty(self) -> bool:
        return self.a.empty() and self.b.empty()
