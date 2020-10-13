class Node:
    # Initialize Node
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        # if data already exists (in the form of a node) than return false
        if self.value == data:
            return False
        # if data is less than current node than ignore the right
        elif self.value > data:
            # if there is a left child than call insert again on left child
            if self.leftChild:
                return self.leftChild.insert(data)
            # if there is no left child add one to be a node containing data
            else:
                self.leftChild = Node(data)
                return True
        # if inserted value is larger than current node than ignore the left
        else:
            # if we have a right child call insert again on it
            if self.rightChild:
                return self.rightChild.insert(data)
            # if there is no right child than insert data there
            else:
                self.rightChild = Node(data)
                return True

    def getSize(self):
        if self.leftChild and self.rightChild:
            return 1 + self.leftChild.getSize() + self.rightChild.getSize()
        elif self.leftChild:
            return 1 + self.leftChild.getSize()
        elif self.rightChild:
            return 1 + self.rightChild.getSize()
        else:
            return 1

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preoder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

    def find(self, data):
        # if value of current node is equal to data (we have found the data)
        if self.value == data:
            return True
        # search left side
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        # search right side
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def getHeight(self):
        if self.letChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1


class Tree:
    def __init__(self):
        self.root = None

    # Get height of search tree
    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0

    # Find number of nodes in a tree
    def getSize(self):
        if self.root:
            return self.root.getSize()
        else:
            return 0

    # Insert a value into tree
    def insert(self, data):
        # if there is no root than call the insert function on root node
        if self.root:
            return self.root.insert(data)
        # new root becomes a node of the data
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        # if tree is empty than return false
        else:
            return False

    # print preorder traversal
    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    # print postorder traversal
    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    # print inorder traversal
    def inorder(self):
        print("InOrder")
        self.root.inorder()

    # def depth_first(self):

    def breath_first(self):
        # Base Case
        if self.root is None:
            return

        # Create an empty queue for level order traversal
        queue = []

        # Enqueue Root and initialize height
        queue.append(self.root)

        while(len(queue) > 0):
            # Print front of queue and remove it from queue
            print(queue[0].value)
            node = queue.pop(0)

            # Enqueue left child
            if node.leftChild is not None:
                queue.append(node.leftChild)

            # Enqueue right child
            if node.rightChild is not None:
                queue.append(node.rightChild)

    # remove
    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # if data is in root node
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChiled is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.value = delNode.value

                # delete delNode (we know it doesn't have left child or two children because we are at most left-hand side of tree)
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChiled = None
                    else:
                        delNodeParent.rightChiled = None

        parent = None
        node = self.root
        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove-node has no children:
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        # case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNode.Parent = delNode
                delNode = delNode.leftChild

            node.value = delNode.value
            # delete delNode (we know it doesn't have left child or two children because we are at most left-hand side of tree)
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.leftChiled = None
                else:
                    delNodeParent.rightChiled = None
