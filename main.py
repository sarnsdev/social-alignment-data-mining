from src.Graph import Graph

def main():
    graph_file = (open("./data/CA-GrQc.txt", "r")).read()
    graph = Graph(graph_file)


if __name__ == '__main__':
    main()
