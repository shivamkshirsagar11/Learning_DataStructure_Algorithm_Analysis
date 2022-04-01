import Edgeandweight as E
def main():
    edges,vertex,D = E.EdgeVertexAndDmatrix()
    BellmanFordShortestPath(edges,vertex,D)
    return

def BellmanFordShortestPath(edge,vertex,d):
    v = len(vertex)
    for i in range(0,v-1):
        for e in edge:
            if d[E.index(d,e.v1)].distance != E.inf and (d[E.index(d,e.v1)].distance + e.weight < d[E.index(d,e.v2)].distance):
                d[E.index(d,e.v2)].distance = d[E.index(d,e.v1)].distance + e.weight
        for i in d:
            print(i)
        print("----------------------------")
    for i in range(v):
        for e in edge:
            if d[E.index(d,e.v1)].distance != E.inf and d[E.index(d,e.v1)].distance + e.weight < d[E.index(d,e.v2)].distance:
                print("there's an -ve edge cycle in graph")
                return
    print("Vertex   Distance from source")
    for i in d:
        print(i)

main()
