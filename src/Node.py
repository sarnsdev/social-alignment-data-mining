class Node(object):
    """docstring for Node."""
    def __init__(self):
        super(Node, self).__init__()
        self.edges = [] # int value of the nodes it is connected to

    def add(self, value):
        if value not in self.edges:
            self.edges.append(value)

    def remove(self, value):
        if value in self.edges:
            self.edges.remove(value)

    def get_edges(self):
        return list(self.edges)
