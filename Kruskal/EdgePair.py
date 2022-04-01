class Edge:
    v1 = 0
    v2 = 0
    weight = 0
    def __init__(self,v1,v2,w):
        self.v1 = v1
        self.v2 = v2
        self.weight = w
edges = []
def makeEdgePair(v1,v2,w):
    edges.append(Edge(v1,v2,w))

def sortEdgeByWeight(edgespair): 
    for i in range(len(edgespair)-1):
        for j in range(i+1,len(edgespair)): 
            if edgespair[i].weight > edgespair[j].weight:
                edgespair[i],edgespair[j] = edgespair[j],edgespair[i]
    return edgespair

def printMst(mst): 
    w = 0
    print("Minimum Spanning Tree:-")
    for i in mst: 
        print(i.v1,end=" --> ")
        print(i.v2,end="| Weight: ")
        print(i.weight)
        w += i.weight
    print("Total Weight: ",end="")
    print(w)
    return