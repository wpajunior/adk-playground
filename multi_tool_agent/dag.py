from enum import Enum, auto


class NodeType(Enum):
    DATA_EVALUATION = auto()
    ACTION_EXECUTION = auto()
    USER_INPUT = auto()


class Node:
    def __init__(self, step: int, type: NodeType):
        self.step = step
        self.type = type
        self.content: str = ""

    def get_content(self) -> str:
        return self.content

    def __repr__(self):
        return f"Node({self.step})"

    def __hash__(self):
        return hash(self.step)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.name == other.name
        return False


class DAG:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node: Node):
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, from_node: Node, to_node: Node):
        if from_node in self.edges and to_node in self.edges:
            self.edges[from_node].append(to_node)

    def __repr__(self):
        return f"DAG(nodes={self.nodes}, edges={self.edges})"
