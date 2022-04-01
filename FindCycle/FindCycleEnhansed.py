import EdgePair as e,Parent as p,UnionEnhanced as ue,FindEnhanced as fe
import sys
import time
sys.setrecursionlimit(10**6)
def isCycle(edges,parents): 
    for i in edges: 
        p1 = fe.findAbsoluteParent(parents,i.v1)
        p2 = fe.findAbsoluteParent(parents,i.v2)
        if p1==p2 and p1 != -1 and p2 != -1 :
            return True
        else:
            ue.union(parents,i.v1,i.v2)
    return False
def main(): 
    n = int(input("How many vertex?: "))
    for i in range(n): 
        p.setParentRefresh(int(input("Vertex: ")))
    n = int(input("How many Edges?: "))
    for i in range(n): 
        e1 = int(input("Edge End point 1: "))
        e2 = int(input("Edge End point 2: "))
        e.makeEdgePair(e1,e2)
        print("----------next Edge----------")
    start_time = time.time()
    if isCycle(e.edges,p.parents): 
        print("YES, it forms a cycle in graph!")
    else :
        print("No, it does not form a cycle in graph!")
    print("--- %s seconds ---" % (time.time() - start_time))
    fe.printf(p.parents)
main()