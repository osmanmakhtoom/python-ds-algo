from typing import Any

from node import Node


class DoublyNode(Node):
    """ Node class included previous node pointer for using in doubly linkedlist """

    def __init__(self, data: Any = None) -> None:
        super().__init__(data)
        self.previous = None
