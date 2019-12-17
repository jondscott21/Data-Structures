import sys
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
            return self
        if self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target, cache={'returned': False}):
        print(self.value, target)
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                cache['returned'] = False
                return cache['returned']
            elif self.left.value == target:
                cache['returned'] = True
                return cache['returned']
            else:
                self.left.contains(target)
        elif self.value < target:
            if self.right is None:
                cache['returned'] = False
                return cache['returned']
            elif self.right.value == target:
                cache['returned'] = True
                return cache['returned']
            else:
                self.right.contains(target)
        return cache['returned']

    # Return the maximum value found in the tree
    def get_max(self, cache={'max_val': 0}):
        if self.right is None:
            cache['max_val'] = self.value
            return cache['max_val']
        else:
            self.right.get_max()
        return cache['max_val']
            

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

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
# print(bst.contains(6))
# print(bst.contains(8))
# print(bst.left.right.value)
# print(bst.right.left.value)

print(bst.get_max())
bst.insert(30)
print(bst.get_max())
bst.insert(300)
bst.insert(3)
print(bst.get_max())