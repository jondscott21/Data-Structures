import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # it gives us a nice list allows us access to a solid FIFO structure
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size = self.storage.length

    def dequeue(self):
        value = self.storage.remove_from_tail()
        self.size = self.storage.length
        return value

    def len(self):
        return self.size
