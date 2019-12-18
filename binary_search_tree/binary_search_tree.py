import sys
import random
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
            return self.value
        if self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # print(self.value, target)
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
            

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
        return

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BinarySearchTree(5)

# bst.insert(2)
# bst.insert(3)
# bst.insert(6)
# bst.insert(7)
# bst.insert(10)
# print(bst.contains(10))
# print(bst.contains(8))
# print(bst.left.right.value)
# print(bst.right.left.value)

# print(bst.get_max())
# bst.insert(30)
# print(bst.get_max())
# bst.insert(300)
# bst.insert(3)
# print(bst.get_max())

arr = []
cb = lambda x: arr.append(x)

v1 = random.randint(1, 101)
v2 = random.randint(1, 101)
v3 = random.randint(1, 101)
v4 = random.randint(1, 101)
v5 = random.randint(1, 101)

bst.insert(v1)
bst.insert(v2)
bst.insert(v3)
bst.insert(v4)
bst.insert(v5)

bst.for_each(cb)

print('5: ', 5, 5 in arr)
print('v1: ', v1, v1 in arr)
print('v2: ', v2, v2 in arr)
print('v3: ', v3, v3 in arr)
print('v4: ', v4, v4 in arr)
print('v5: ', v5, v5 in arr)