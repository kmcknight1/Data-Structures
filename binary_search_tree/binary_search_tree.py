from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        # self is a node (not the entire tree)
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # This method is done recursively, checking if there are valid nodes to the left or right
    # depending on whether the value is less than or greater than self.value
    # if there is a node in that position, the value will be sent back into the insert function
    # this will happen until there is no value found (aka, a parking spot) at which point
    # an instance of BinarySearchTree will be created in that spot
    def insert(self, value):
        # self.left and/or self.right need to be valid nodes to call insert on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            else:
                # found parking spot (base case)
                self.left = BinarySearchTree(value)
        else:
            # if value is >= self.value, check for valid node, if found: insert(), if not: park
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # base case: if the target == self.value then True, the target is in the BST
        if target == self.value:
            return True

        # check for valid node on left if target is < self.value
        if self.left and target < self.value:
            # recursively call contains function on self.left passing in the target
            return self.left.contains(target)
        # check for valid node on the right if target is > self.value
        elif self.right and target > self.value:
            # recursively call contains function on self.right passing in the target
            return self.right.contains(target)
        # if no conditions above are true, the target is not found, return False
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        # base case: if no nodes to the right, max value must be self.value
        if not self.right:
            return self.value
        # if there are nodes to the right, recursively call get_max on self.right
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # if both self.right and self.left
        if self.right and self.left:
            # run cb on self.value
            cb(self.value)
            # recursively call for_each on both right and left nodes, passing in the cb
            self.right.for_each(cb)
            self.left.for_each(cb)
        elif self.left:
            cb(self.value)
            self.left.for_each(cb)
        elif self.right:
            cb(self.value)
            self.right.for_each(cb)
        else:
            cb(self.value)

    # iterative for_each approach
    # DEPTH FIRST

    def iterative_for_each(self, cb):
        stack = []
        # add the root of the tree to the stack so the loop will start running
        stack.append(self)

        # loop as long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

        # DAY 2 Project -----------------------

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if not node:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        temp_node = None

        queue.enqueue(node)

        while queue.len() > 0:
            temp_node = queue.dequeue()
            print(temp_node.value)

            if temp_node.right:
                queue.enqueue(temp_node.right)

            if temp_node.left:
                queue.enqueue(temp_node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        temp_node = None
        stack.push(node)
        while stack.len() > 0:
            temp_node = stack.pop()
            print(temp_node.value)
            if temp_node.right:
                stack.push(temp_node.right)
            if temp_node.left:
                stack.push(temp_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
