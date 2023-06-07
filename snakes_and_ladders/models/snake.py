class Snake:

    def __init__(self, head=None, tail=None):
        self.head: int = head
        self.tail: int = tail

    def get_head(self) -> int:
        return self.head

    def set_head(self, head) -> None:
        self.head = head

    def get_tail(self) -> int:
        return self.tail

    def set_tail(self, tail) -> None:
        self.tail = tail
