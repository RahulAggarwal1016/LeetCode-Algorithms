# Implementing a doubly linked list
# use more memory than normal linked lists

class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_prev(self):
        return self.prev_node

    def set_prev(self, p):
        self.prev_node = p

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class DoublyLinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        if self.root:
            self.root.set_prev(new_node)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root

        while this_node:
            if this_node.get_data() == d:
                next_node = this_node.get_next()
                prev_node = this_node.get_prev()

                if next_node:
                    next_node.set_prev(prev_node)
                if prev_node:
                    prev_node.set_next(next_node)

                # set new root
                if this_node == self.root:
                    self.root = this_node.get_next()
                elif this_node.get_next().get_prev() is None:
                    self.root = this_node.get_next()
                else:
                    self.root = this_node
                self.size -= 1
                return True  # data removed
            else:
                this_node = this_node.get_next()
        return False  # data not found

    # find data in a linked list
    def find(self, d):
        this_node = self.root
        # iterate through values
        while this_node is not None:
            # if current node equals data, return the data
            if this_node.get_data() == d:
                return d
            # if we at last node in linked list return False (we have gone through all nodes)
            elif this_node.get_next() == None:
                return False
            else:
                # search the next node
                this_node = this_node.get_next()
