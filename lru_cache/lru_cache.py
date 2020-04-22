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
        # storage is a dictionary with corresponding keys as they were set
        # and the value to the key is a NODE, which is in the DLL
        # i.e. self.storage[key] will point to an actual node
        # self.storage[key].value will be a tuple, containing the key and value
        #self.storage[key].value[0] == key
        #self.storage[key].value[1] == value
        # self.storage[key].next == next node in the DLL (or None)
        # self.storage[key].prev == previous node in the DLL (or None)
        self.storage = {}
        self.DLL = DoublyLinkedList()

    def __str__(self):
        if self.storage == {}:
            return "\nNOTHING IN STORAGE"
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
            return f"\nLIMIT: {self.limit} \nCACHE: {pairs} \nTAIL(LRU): {tail} \nHEAD(MRU): {head}"

    def __len__(self):
        return len(self.DLL)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if in storage, get the value
        # move it to the head of the list
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
                # if not in storage, remove storage tail
                del self.storage[self.DLL.tail.value[0]]

            self.DLL.remove_from_tail()  # remove tail from DLL
            self.DLL.add_to_head((key, value))  # add new value to head
            self.storage[key] = self.DLL.head  # add value to storage

        else:
            self.DLL.add_to_head((key, value))
            self.storage[key] = self.DLL.head


# create instance of LRU, passing in a limit
cache = LRUCache(4)

# print empty list
print(str(cache))
# print the length
print(len(cache))

# set some key:value pairs
cache.set("a", 1)
print(str(cache))

cache.set("b", 2)
print(str(cache))
print(len(cache))

# set a couple more
cache.set("c", 3)
cache.set("d", 4)
print(str(cache))
print(len(cache))

cache.set("e", 5)

print(str(cache))

cache.set("c", 6)

print(str(cache))
