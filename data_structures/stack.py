# implementing a stack

class Stack:
    def __init__(self):
        self.stack = []

    # add item to stack
    def push(self, item):
        self.stack.append(item)

    # remove top most value off stack (Last In First Out - LIFO)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    # look at top item on stack without taking it off
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)
