class EdgeList :
    __v1 = 0
    __v2 = 0
    def __init__(self,v1=-1,v2=-1):
        self.__v1 = v1
        self.__v2 = v2
    def __str__(self):
        return str(self.__v1)+" --> "+str(self.__v2)
    def getV1(self):
        return self.__v1
    def getV2(self):
        return self.__v2

class Graph:
    __edges = []

    def addEdgePair(self,v1,v2):
        self.__edges.append(EdgeList(v1,v2))

    def __str__(self):
        num, arr = self.numberOfVertex()
        print("---graph start---")
        print("Total "+str(num)+" vertex",end=": ")
        print(arr)
        for i in self.__edges:
            print(i)
        return "---graph end---"

    def numberOfVertex(self):
        vertex = []
        for i in self.__edges:
            v1  = i.getV1()
            v2 = i.getV2()
            if v1 not in vertex:
                vertex.append(v1)
            if v2 not in vertex:
                vertex.append(v2)
        return len(vertex) ,vertex

    def findJoinedEdges(self,vertex):
        temp = []
        for i in self.__edges:
            if i.getV1() == vertex: temp.append(i.getV2())
            elif i.getV2() == vertex: temp.append(i.getV1())
        return temp

class Coloring:
    v = 0
    color= 0

    def __init__(self,v=-1,color=-1):
        self.v = v
        self.color = color
    def __str__(self):
        return "vertex: "+str(self.v)+" color: "+str(self.color)


def makeAdjList(graphObj):
    num, arr = graphObj.numberOfVertex()
    adjmatrix = []
    for i in range(num):
        adj = graphObj.findJoinedEdges(arr[i])
        adjmatrix.append([arr[i],adj])
    return adjmatrix

def printAdjMat(mat):
    for i in mat:
        print(i[0],end=" --> ")
        print(i[1])

def findColor(color,vertex):
    for i in color:
        if i.v == vertex : return i.color

def setColor(color,vertex,setcolor):
    for i in color:
        if i.v == vertex : i.color = setcolor

def GraphColoring(adj,color):
    temp = 0
    for i in adj:
        vertex = i[0]
        adjofvertex = i[1]
        colors = []
        for adjs in adjofvertex:
            colors.append(findColor(color,adjs))
        # print(colors)
        if temp not in colors:
            t = 0
            for j in range(temp):
                if j not in colors:
                    t = t+1
                    setColor(color,vertex,j)
                    break
            if t == 0:
                setColor(color,vertex,temp)
        else:
            t = 0
            for j in range(temp):
                if j not in colors:
                    t = t+1
                    setColor(color,vertex,j)
                    break
            # print(t)
            if t == 0:
                temp = temp+1
                setColor(color,vertex,temp)
    for i in color:
        print(i)

def main():
    graph = Graph()
    n = int(input("total edges: "))
    for i in range(n):
        edgeTemp = input("v1 and v2 ...")
        edgeTemp = edgeTemp.split()
        v1 = int(edgeTemp[0])
        v2 = int(edgeTemp[1])
        graph.addEdgePair(v1,v2)
    num, arr = graph.numberOfVertex()
    adjMatrix = makeAdjList(graph)
    printAdjMat(adjMatrix)
    color = [Coloring() for i in range(num)]
    for i in range(num):
        color[i].v = arr[i]
    GraphColoring(adjMatrix,color)
main()