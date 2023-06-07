from .eviction_policy_interface import EvictionPolicyInterface
from cache_lld.algorithms.doubly_linked_list import DoublyLinkedList


class LRUEvictionPolicy(EvictionPolicyInterface):

    def __init__(self):
        self.dll = DoublyLinkedList()

        # Used to store the relation b/w key and its reference in dll
        self.map = {}  # key: any, value: node.

    def key_accessed(self, key: any) -> None:
        """
        When key is accessed, we move that key towards end of dll
        This ensures that front of dll will always have least recently used node
        """
        if key in self.map.keys():
            self.dll.detach_node(self.map[key])
            self.dll.add_node_at_last(self.map[key])
        else:
            new_node = self.dll.add_element_at_last(key)
            self.map[key] = new_node

    def evict(self) -> None:
        """
        Remove first element from dll since it is least recently used
        """
        first_node = self.dll.get_first_node()
        if not first_node:
            return None
        self.dll.detach_node(first_node)
        return first_node.get_value()
