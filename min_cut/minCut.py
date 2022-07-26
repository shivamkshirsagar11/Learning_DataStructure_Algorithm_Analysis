from edge_util import EdgeUtil
import math
def MinCut(graph_obj,n):
    minc = math.inf
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
        # print(minc)
        # print(obj.Cook())
    # print(obj.Cook())
    # print(obj.concat_vertices())
    return minc


if __name__ == '__main__':
    which = input("1) directed\n2) undirected\nEnter: ")
    if int(which) > 2 or int(which)< 1:print("Couldn't Understand what you're looking for\nTry:\n1) directed\n2)undirected\n:-)")
    else:
        key = EdgeUtil(int(which),[])
        adj = key.Cook()
        # for i in range(0,2):
        #     print("------------------------------")
        #     random_vert_index = key.random_node()
        #     random_vert_edge = key.random_edge_from_random_node(random_vert_index)
        #     random_edge = (adj[random_vert_index][0],adj[random_vert_index][1][random_vert_edge][0])
        #     for i in adj:print(i)
        #     print(f'random edge: {random_edge}')
        #     key.contract_edge(random_edge)
        #     adj = key.Cook()
        #     for i in adj:print(i)
        print(f'MIn Cut of given graph is: {MinCut(key,key.total_vertices())}')

        