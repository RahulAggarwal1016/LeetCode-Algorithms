# implenting a queue

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # add item to front of queue (First In First Out - FIFO)
    def enqueue(self, item):
        self.items.insert(0, item)

    # remove last item in queue
    def dequeue(self):
        if self.items:
            return self.items.pop()
        else:
            return False

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
