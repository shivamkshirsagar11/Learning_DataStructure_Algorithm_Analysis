from math import inf
class Edge: 
    v1 = 0
    v2 = 0
    weight = 0
    def __init__(self,v1,v2,w):
        self.v1 = v1
        self.v2 = v2
        self.weight = w
class Dmat:
    vertex = 0
    distance = 0
    def __init__(self,vertex,distance):
        self.vertex = vertex
        self.distance = distance
    def __str__(self):
        return str(self.vertex)+"           "+str(self.distance)

def EdgeVertexAndDmatrix():
    edges = []
    edges.append(Edge(1,2,-3))
    edges.append(Edge(2,5,4))
    edges.append(Edge(5,4,-9))
    edges.append(Edge(4,3,8))
    edges.append(Edge(1,3,5))
    edges.append(Edge(2,3,1))
    edges.append(Edge(2,4,7))
    edges.append(Edge(4,2,-2))
    vertex,Dmatrix = GiveMeVertex(edges)
    return edges,vertex,Dmatrix

def GiveMeVertex(edge):
    vert = []
    Dmatrix = []
    for i in edge:
        if i.v1 not in vert:
            vert.append(i.v1)
        if i.v2 not in vert:
            vert.append(i.v2)
    for i in vert:
      Dmatrix.append(Dmat(i,0 if i==1 else inf))
    return vert,Dmatrix

def index(dm,key):
    ind = 0
    for i in dm:
        if i.vertex == key:
            return ind
        ind += 1
    return None

# def main():
#     edges,vertex,d = EdgeVertexAndDmatrix()
#     print(d[index(d,4)])
# main()
