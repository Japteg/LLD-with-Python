class Node:

    """
    Represents the node in doubly linked list (DLL).
    A single node is expected to be created for each element that needs to be inserted
    in DLL
    """

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_prev(self):
        return self.prev

    def set_prev(self, prev_link):
        self.prev = prev_link

    def get_next(self):
        return self.next

    def set_next(self, next_link):
        self.next = next_link
