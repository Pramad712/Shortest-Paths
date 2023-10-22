from heapq import heappop, heappush
from graph import Node, NodePathData

# similar to https://docs.python.org/3.11/library/heapq.html, but modified for this implementation of A*

class PriorityQueue:
    def __init__(self):
        self.heap: list[NodePathData] = []
        self.node_to_item: dict[Node, NodePathData] = {}

    def add(self, value: NodePathData):
        if value.node in self.node_to_item:
            original = self.node_to_item.get(value.node)

            if value < original:
                self.update(self.node_to_item.get(value.node), value)

            return

        heappush(self.heap, value)
        self.node_to_item[value.node] = value

    def remove(self, value: NodePathData):
        if value.node not in self.node_to_item:
            raise KeyError(f"{value} not found")

        del self.node_to_item[value.node]
        value.node = None

    def update(self, value: NodePathData, new_value: NodePathData):
        self.remove(value)
        self.add(new_value)

    def peek(self) -> NodePathData: # Will not be used in this project, but made just for completeness
        while self.heap:
            extracted = self.heap[0]

            if extracted.node is not None:
                return extracted

            else:
                # No remove from self.node_to_item necessary since the only way first.node is None is if self.remove() was called (line 24), in which the node is removed from self.node_to_item
                heappop(self.heap)

        raise KeyError("Peeking into an empty priority queue")

    def pop(self) -> NodePathData:
        while self.heap:
            extracted = heappop(self.heap)

            if extracted.node is not None:
                del self.node_to_item[extracted.node]
                return extracted

        raise KeyError("Popping from an empty priority queue")
