from doubly_linked_list import DoublyLinkedList


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
        self.storage = {}
        self.DLL = DoublyLinkedList()

    def __str__(self):
        if self.storage == {}:
            return
        else:
            pairs = []
            tail = None
            head = None
            for i in self.storage:
                pairs.append(self.storage[i].value)
                if self.storage[i].next == None:
                    tail = self.storage[i].value
                if self.storage[i].prev == None:
                    head = self.storage[i].value
            return f"LIMIT: {self.limit} \nCACHE: {pairs} \nTAIL(LRU): {tail} \nHEAD(MRU): {head}"

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # get the value
        # move it to the tail of the list
        # return the value
        if key not in self.storage:
            return None

        self.DLL.move_to_front(self.storage[key])
        return self.storage[key].value[1]

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
        # add key value pair to storage
        # make it MRU (tail)
        # if already at limit, remove head
        # if key already exists, overwrite the value with the new value
        if len(self.DLL) == self.limit:
            if key not in self.storage:
                del self.storage[self.DLL.tail.value[0]]

            self.DLL.remove_from_tail()
            self.DLL.add_to_head((key, value))
            self.storage[key] = self.DLL.head

        else:
            self.DLL.add_to_head((key, value))
            self.storage[key] = self.DLL.head


cache = LRUCache(4)
cache.set("a", 1)
cache.set("b", 2)
cache.set("c", 3)
cache.set("d", 4)

print(str(cache))

cache.set("e", 5)

print(str(cache))

cache.set("c", 6)

print(str(cache))
