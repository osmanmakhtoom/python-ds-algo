from typing import Any

from memory_profiler import profile

from doubly_node import DoublyNode
from singly_linked_list import SinglyLinkedList


class DoublyLinkedList(SinglyLinkedList):
    """ Doubly linked list for chaining nodes with two pointers """

    @profile
    def __init__(self) -> None:
        """ Initialize DoublyLinkedList's current instance """
        super().__init__()

    @profile
    def insert(self, index: int, data: Any) -> DoublyNode:
        """ Insert new node at given index of DoublyLinkedList's current instance """
        node = DoublyNode(data)
        if index > self.len:
            raise ValueError("Index out of range")
        elif index == 0:
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.len += 1
        elif index == self.len:
            self.append(data)
        else:
            prev = self.head
            for count, current in enumerate(self):
                if index == count:
                    node.next = current
                    current.previous = node
                    node.previous = prev
                    prev.next = node
                    self.len += 1
                    break
                prev = current
        return node

    @profile
    def append(self, data: Any) -> DoublyNode:
        """ Insert new node at end of DoublyLinkedList's current instance """
        node = DoublyNode(data)
        if self.tail:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.len += 1
        return node

    @profile
    def pop(self, index: int = -1) -> DoublyNode:
        """ Remove and return node by given index or last node from DoublyLinkedList's current instance """
        if self.head is None:
            raise ValueError("No data in this list, we need at least one item")
        elif index > self.len:
            raise ValueError("Index out of range")
        elif index == 0:
            current = self.head
            self.head = current.next
            self.head.previous = None
            self.len -= 1
            return current
        elif index == -1 or index == self.len - 1:
            current = self.tail
            prev = current.previous
            self.tail = prev
            self.tail.next = None
            self.len -= 1
            return current
        else:
            prev = self[index - 1]
            current = prev.next
            prev.next = current.next
            current.next.previous = prev
            self.len -= 1
            return current
