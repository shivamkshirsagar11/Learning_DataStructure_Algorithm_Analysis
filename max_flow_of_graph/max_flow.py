from edge_util import EdgeUtil
def All_path_DFS(arr,obj,node,dest_node,visited,curr):
    visited.append(node)
    if node[0] == dest_node:
        for i in visited:
            curr[-1].append(i)
        curr.append([])
    else:
        index = obj.find(node[0],False)
        neighbours = arr[index][1]
        for i in neighbours:
            if i[0] not in visited:
                curr = All_path_DFS(arr,obj,i,dest_node,visited,curr)
    visited.pop()
    return curr
if __name__ == '__main__':
    which = input("1) directed\n2) undirected\nEnter: ")
    if int(which) > 2 or int(which)< 1:print("Couldn't Understand what you're looking for\nTry:\n1) directed\n2)undirected\n:-)")
    else:
        key = EdgeUtil(int(which))
        adj = key.Cook()
        a2 = All_path_DFS(adj,key,'S','T',[],[[]])
        print("All possible paths: ")
        a2.pop()
        for i in a2:
            print(i)
