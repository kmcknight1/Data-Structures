from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    # FIFO (first in first out)
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add item to the end
        self.storage.add_to_tail(value)

    def dequeue(self):
        # remove item from front and return the item
        if not self.storage.head:
            return
        return self.storage.remove_from_head()

    def len(self):
        # returns number of items in queue
        return len(self.storage)
