class EdgeUtil:
    from random import randint
    def __init__(self,param):
        self.__adj_arr = self.start(param)

    def check_index(self,arr,key):
        for index,i in enumerate(arr):
            if i[0] == key: return index
        return None

    def give_adj_list_directed(self,arr):
        adj = []
        for i in arr:
            index = self.check_index(adj,i[0])
            if index != None:
                adj[index][1].append((i[1],i[2]))
            else:
                adj.append((i[0],[(i[1],i[2])]))
        return adj
    
    def give_adj_list_Undirected(self,arr):
        adj = []
        adj_check = []
        for i in arr:
            if i[0] not in adj_check: 
                adj.append((i[0],[]))
                adj_check.append(i[0])
            if i[1] not in adj_check: 
                adj.append((i[1],[]))
                adj_check.append(i[1])
        adj_check.clear()
        for i in arr:
            index1 = self.check_index(adj,i[0])
            index2 = self.check_index(adj,i[1])
            if index1 != None:
                if (i[1],i[2]) not in adj[index1][1]:
                    adj[index1][1].append((i[1],i[2])) 
                else:continue
            else:
                adj.append((i[0],[(i[1],i[2])]))
            if index2 != None:
                if (i[0],i[2]) not in adj[index2][1]:
                    adj[index2][1].append((i[0],i[2])) 
                else:continue
            else:
                adj.append((i[1],[(i[0],i[2])]))
        return adj

    def start(self,test):
        print("Enter # to stop")
        choice = 0
        arr = []
        node = []
        while(True):
            choice = input("Enter Edge and weight: ")
            if choice == '#':break
            choice = choice.split()
            arr.append((choice[0], choice[1], int(choice[2])))
        if test == 1:
            return self.give_adj_list_directed(arr)
        elif test == 2: return self.give_adj_list_Undirected(arr)
        else: return None

    def Cook(self): return self.__adj_arr

    def find(self,key,deep_find):
        if deep_find:
            for index,i in enumerate(self.__adj_arr):
                for j in i[1]:
                    if j[0] == key: return index
        else:
            return self.check_index(self.__adj_arr,key)
        return None
    def random_node(self):
        return self.randint(0,len(self.__adj_arr)-1)
    
    def random_edge_from_random_node(self,random_index):
        length_edges = len(self.__adj_arr[random_index][1]) - 1
        return self.randint(0,length_edges)

    def total_vertices(self):
        return len(self.__adj_arr)

    def remove_edge(self,vertex,remove_edge):
        index = self.find(vertex,False)
        for i in self.__adj_arr[index][1]:
            if i[0] == remove_edge:
                self.__adj_arr[index][1].remove(i)

    def contract_edge(self,edge):
        self.remove_edge(edge[0],edge[1])
        self.remove_edge(edge[1],edge[0])
        index1 = self.find(edge[0],False)
        index2 = self.find(edge[1],False)
        for i in self.__adj_arr[index2][1]:
            self.__adj_arr[index1][1].append(i)
        self.__adj_arr[index1][1].append(("Concated",edge[0],edge[1]))
        self.__adj_arr.remove(self.__adj_arr[index2])

    def total_edges(self):
        l = 0
        for i in self.__adj_arr:
            l = len(i[1])
            if i[1][-1][0] == "Concated": l = l-1
        return l

        
