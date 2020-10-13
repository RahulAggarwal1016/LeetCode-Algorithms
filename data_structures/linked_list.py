class Node:
    # initialize node
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    # get next node
    def get_next(self):
        return self.next_node

    # set next node
    def set_next(self, n):
        # override next node if given upon creation
        self.next_node = n

    # get current node
    def get_data(self):
        return self.data

    # set current node
    def set_data(self, d):
        self.data = d

    # convert node to a string
    def to_string(self):
        return "Node Value: " + str(self.data)


class LinkedList:
    # initialize linked list
    def __init__(self):
        self.root = None
        self.size = 0

    # get length of linked list
    def get_size(self):
        return self.size

    # add a value (then turned into a node) to front of linked list ---> This is different than trying to directly add a node (will clash since we already make a new node)
    def add(self, d):
        # create a new node and set current
        if self.size == 0:
            new_node = Node(d)
            self.root = new_node
        else:
            new_node = Node(d, self.root)
            self.root = new_node
            self.size += 1

    # def add_node(self, n):
    #     n.set_next(self.root)
    #     self.root = n
    #     self.size += 1

    # remove a node
    def remove(self, d):
        this_node = self.root
        prev_node = None

        # while we are not at end of linked list
        while this_node is not None:
            # if we find node we are looking for
            if this_node.get_data() == d:
                # if we find node and it has a previous node, set previous node's next value to be the current node's next (since it will be gone)
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    # previous node can only be blank if root node the one we want to remove, set root to be the linked_list[1] node
                    self.root = this_node.get_next()
                self.size -= 1
                return True  # data removed
            else:
                prev_node = this_node
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

    # print linked list
    def print_list(self):
        print("Print List......")
        # if linked list is empty
        if self.root is None:
            return

        this_node = self.root
        print(this_node.to_string())

        # if node has a next node (i.e. not at end)
        while this_node.get_next():
            this_node = this_node.get_next()
            print(this_node.to_string())

    # sort linked list
    def sort(self):
        if self.size > 1:
            new_list = []
            current = self.root
            new_list.append(current)
            while current.get_next() is not None:
                current = current.get_next()
                new_list.append(current)
            new_list = sorted(
                new_list, key=lambda node: node.get_data(), reverse=True)
            new_linked_list = LinkedList()
            for node in new_list:
                new_linked_list.add(node.get_data())
            return new_linked_list
        return self


myList = LinkedList(4)
myList.add(5)
myList.add(1)
myList.add(4)
myList.add(5)
myList.add(8)
myList.add(99)
