def find(parentList,v):
    for p in parentList:
        if p.vertex == v:
            return p
    return
def findAbsoluteParent(parentList,vertex):
    objParent = find(parentList,vertex)
    if objParent.parent == -1:
        return objParent.vertex
    else:
        return findAbsoluteParent(parentList,objParent.parent)

def findAbsoluteParentUnion(parentList,vertex):
    objParent = find(parentList,vertex)
    if objParent.parent == -1:
        return objParent
    else:
        return findAbsoluteParentUnion(parentList,objParent.parent)

def printf(parentList):
    for i in parentList:
        print(i.vertex,end=" ")
        print(i.parent)
    return