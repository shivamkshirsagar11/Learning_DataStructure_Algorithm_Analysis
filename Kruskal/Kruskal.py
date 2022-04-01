import EdgePair as e,Parent as p,UnionEnhanced as u,FindEnhanced as f
import sys
import time
sys.setrecursionlimit(10**6)
def main(): 
    V = int(input("how many vertex? "))
    for i in range(V) :
        p.setParentRefresh(int(input("vertex...")))
    E = int(input("how many edges? "))
    for i in range(E):
        type = input("Edge1, Edge2, Weight: ")
        type = type.split()
        e.makeEdgePair(int(type[0]),int(type[1]),int(type[2]))
    start_time = time.time()
    sortedEdges = e.sortEdgeByWeight(e.edges)
    MST = kruskalFindMST(sortedEdges,V,E)
    e.printMst(MST)
    # print()
    # f.printf(p.parents)
    print("--- %s seconds ---" % (time.time() - start_time))
    return
def kruskalFindMST(edges,v,e): 
    mst = []
    for ed in edges:
        p1 = f.findAbsoluteParent(p.parents,ed.v1)
        p2 = f.findAbsoluteParent(p.parents,ed.v2)
        if p1 == p2 and p1 != -1 and p2 != -1: 
            continue
        else: 
            u.unionByRank(p.parents,p1,p2)
            mst.append(ed)
    return mst
main()