class Edge:
    v1 = 0
    v2 = 0
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

edges = []
def makeEdgePair(v1,v2):
    edges.append(Edge(v1,v2))