from typing import Any
from memory_profiler import profile
from node import Node


class SinglyLinkedList:
    """ Singly linkedlist for chaining nodes """

    def __init__(self) -> None:
        """ Initialize SinglyLinkedList new instance """
        self.tail = None
        self.head = None

    @profile
    def __iter__(self):
        """ Iterate over SinglyLinkedList's current instance """
        current = self.head
        while current:
            yield current
            current = current.next

    @profile
    def __len__(self):
        """ Return length of SinglyLinkedList's current instance """
        size = 0
        for _ in iter(self):
            size += 1
        return size

    @profile
    def insert(self, index: int, data: Any) -> Node:
        """ Insert new node at given index of SinglyLinkedList's current instance """
        node = Node(data)
        if index > len(self):
            raise ValueError("Index out of range")
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index == len(self):
            self.append(data)
        else:
            prev = self.head
            for count, current in enumerate(self):
                if index == count:
                    node.next = current
                    prev.next = node
                    break
                prev = current
        return node

    @profile
    def __getitem__(self, index: int) -> Node:
        """ get node at given index of SinglyLinkedList's current instance """
        if index > len(self):
            raise ValueError("Index out of range")
        elif index == 0:
            return self.head
        elif index == len(self) - 1:
            return self.tail
        elif index == len(self):
            return self.tail.next
        else:
            for count, current in enumerate(self):
                if index == count:
                    return current

    @profile
    def search(self, data: Any) -> int:
        """ Return index of node or -1 by searching given data in SinglyLinkedList's current instance """
        if self.head is None:
            raise ValueError("No data in this list, we need at least one item")
        else:
            for index, node in enumerate(self):
                if data == node.data:
                    return index
            return -1

    @profile
    def append(self, data: Any) -> Node:
        """ Insert new node at end of SinglyLinkedList's current instance """
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        return node

    @profile
    def pop(self, index: int = -1) -> Node:
        """ Remove and return node by given index or last node from SinglyLinkedList's current instance """
        if self.head is None:
            raise ValueError("No data in this list, we need at least one item")
        elif index > len(self):
            raise ValueError("Index out of range")
        elif index == 0:
            current = self.head
            self.head = current.next
            return current
        elif index == -1 or index == len(self) - 1:
            current = self.tail
            prev = self[len(self) - 2]
            self.tail = prev
            self.tail.next = None
            return current
        else:
            prev = self[index - 1]
            current = prev.next
            prev.next = current.next
            return current

    @profile
    def clear(self) -> None:
        """ Clear all nodes from SinglyLinkedList's current instance """
        self.head = None
        self.tail = None


nodes = SinglyLinkedList()
nodes.append([1, 2, 3])
nodes.append({5, 6, 7})
nodes.append("Hi")
nodes.append({"ID": 1, "name": "Osman", "last_name": "Makhtoom"})
nodes.insert(3, [4, "Hi there"])
nodes.insert(len(nodes), [5, 6, 7, 8, 9, "Bye"])

for i in iter(nodes):
    print(repr(i))
print(len(nodes))

print(nodes.search([5, 6, 7, 8, "BYE"]))

print(repr(nodes.pop()))
print(len(nodes))

print(repr(nodes.pop(0)))
print(len(nodes))

for i in range(len(nodes)):
    print(repr(nodes[i]))

nodes.clear()
print(len(nodes))
