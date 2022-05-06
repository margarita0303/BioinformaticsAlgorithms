class BaseTree:
    def __init__(self):
        self.all_nodes = []
        self.all_edges = []
        self.root = self.add_node()

    class node:
        def __init__(self, label):
            self.label = label
            self.edges = []
            self.flag = None
            self.depth = 0

    class edge:
        def __init__(self, from_node, to_node, position, length):
            self.from_node = from_node
            self.to_node = to_node
            self.position = position
            self.length = length
    
    def add_node(self):
        newNode = BaseTree.node(len(self.all_nodes))
        self.all_nodes.append(newNode)
        return newNode

    def add_edge(self, from_node, to_node, pos, length):
        newEdge = BaseTree.edge(from_node, to_node, pos, length)
        to_node.depth = from_node.depth + length
        from_node.edges.append(newEdge)
        self.all_edges.append(newEdge)
        return newEdge


class BaseTrie:
    def __init__(self):
        self.all_nodes = []
        self.all_edges = []
        self.root = self.add_node()

    class node:
        def __init__(self, label):
            self.label = label
            self.edges = []
            self.flag = None

    class edge:
        def __init__(self, from_node, to_node, label, position):
            self.from_node = from_node
            self.to_node = to_node
            self.label = label
            self.position = position
    
    def add_node(self):
        newNode = BaseTrie.node(len(self.all_nodes))
        self.all_nodes.append(newNode)
        return newNode

    def add_edge(self, from_node, to_node, label, pos = None):
        newEdge = BaseTrie.edge(from_node, to_node, label, pos)
        from_node.edges.append(newEdge)
        self.all_edges.append(newEdge)
        return newEdge

 
