from src.Node import Node

class Graph(object):
    """docstring for Graph."""
    def __init__(self, graph_file):
        super(Graph, self).__init__()
        # File passed in
        self.graph_file = graph_file

        # Base values used to store data
        self.graph = dict()
        self.edge_count = 0
        self.node_count = 0

        # Actually build the graph
        self.build_graph_from_source()

    def build_graph_from_source(self):
        # Recieve all the string data from the file
        file_list = str(self.graph_file).split("\n")

        # Iterate over all parts of the file except for the last since that will be blank
        for line in file_list[0:-1]:
            # continue if there is a comment character in this line ignore it
            if "#" in line:
                continue

            # split the line into from and to nodes
            pair = line.split("\t")

            to_node = int(pair[0])
            from_node = int(pair[1])

            # make the nodes if they do not exist
            if to_node not in self.graph:
                self.graph[to_node] = Node()
                self.node_count += 1

            if from_node not in self.graph:
                self.graph[from_node] = Node()
                self.node_count += 1

            # add this edge
            self.graph[to_node].add(from_node)
            self.graph[from_node].add(to_node)
            self.edge_count += 1

    def get_node_count(self):
        return self.node_count

    def get_edge_count(self):
        return self.edge_count
