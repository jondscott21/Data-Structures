import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.hash_map = {}
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.hash_map:
            return None
        self.storage.move_to_front(self.hash_map[key])
        return self.hash_map[key].value
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.hash_map:
            self.hash_map[key] = ListNode(value, key)
            self.storage.move_to_front(self.hash_map[key])
        else:
            self.hash_map.update({key: ListNode(value, key)})
            self.storage.add_to_head(self.hash_map[key])
            if self.storage.length > self.limit:
                del_key = self.storage.remove_from_tail()
                del self.hash_map[del_key]