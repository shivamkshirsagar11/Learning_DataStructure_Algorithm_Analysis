from edge_util import EdgeUtil
import math
def MinCut(graph_obj,n):
    minc = math.inf
    instanse = None
    for k in range(1,(100*(n**2))):
        obj = graph_obj
        o_adj = graph_obj.Cook()
        for i in range(0,n-3):
            if(obj.security_check(n)):break
            random_vert_index = obj.random_node()
            random_vert_edge = obj.random_edge_from_random_node(random_vert_index)
            random_edge = (o_adj[random_vert_index][0],o_adj[random_vert_index][1][random_vert_edge][0])
            key.contract_edge(random_edge)
        temp = obj.total_edges()
        if temp < minc:
            minc = temp
            instanse = obj
    return minc,instanse

if __name__ == '__main__':
    which = input("1) directed\n2) undirected\nEnter: ")
    if int(which) > 2 or int(which)< 1:print("Couldn't Understand what you're looking for\nTry:\n1) directed\n2)undirected\n:-)")
    else:
        key = EdgeUtil(int(which),[],-1)
        adj = key.Cook()
        min_cut, temp = MinCut(key,key.total_vertices())
        print(f'------------------------\nMin-Cut of given graph is: {min_cut}')
        print(f'set V is: {temp.V_set()}')
        print(f'set S-V is: [\'{temp.S_V_set()}\']')