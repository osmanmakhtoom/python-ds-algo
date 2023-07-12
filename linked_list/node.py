from datetime import datetime
from typing import Any


class Node:
    """ Node class for using in linkedlist """

    def __init__(self, data: Any = None) -> None:
        self.data = data
        self.next = None
        self.created_at = datetime.now()

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"{self.data} created at: {self.created_at}"
