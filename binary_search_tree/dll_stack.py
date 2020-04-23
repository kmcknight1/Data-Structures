from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    # LIFO (last in first out)
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if not self.storage.tail:
            return
        return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)