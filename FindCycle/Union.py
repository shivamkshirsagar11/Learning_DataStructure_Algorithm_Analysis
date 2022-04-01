import FindBasic as f
def union(parentList,v1,v2):
    parentV2 = f.findAbsoluteParentUnion(parentList,v2)
    parentV2.parent = v1
    return
