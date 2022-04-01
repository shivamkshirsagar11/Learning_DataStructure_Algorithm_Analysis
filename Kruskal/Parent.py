
class Parent: 
    vertex = 0
    parent = 0
    def __init__(self, v,p): 
        self.vertex = v
        self.parent = p

parents = [] 

def setParentRefresh(v): 
    parents.append(Parent(v,-1))
