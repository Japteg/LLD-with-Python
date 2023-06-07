from .dll_node import Node


class DoublyLinkedList:

    """
    Head->A->B->C->D->E->Tail
    Actual items are enclosed between head and tail nodes
    """

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        # Initially there are no items, so head and tail are joined
        self.head.next = self.tail
        self.tail.prev = self.head

    @staticmethod
    def detach_node(node: Node):
        """
        Node is removed from linked list by modifying pointers
        :param node: node to be removed
        """
        if node:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

    def add_node_at_last(self, node: Node) -> None:
        """
        A->B->C->Tail ==> A->B->C->node->Tail
        """
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.next = self.tail
        node.prev = tail_prev
        self.tail.prev = node

    def add_element_at_last(self, value) -> Node:
        new_node = Node(value)
        self.add_node_at_last(new_node)
        return new_node

    def is_item_present(self) -> bool:
        return self.head != self.tail

    def get_first_node(self) -> Node or None:
        if self.is_item_present():
            return self.head.next
        return None

    def get_last_node(self) -> Node or None:
        if self.is_item_present():
            return self.tail.prev
        return None
