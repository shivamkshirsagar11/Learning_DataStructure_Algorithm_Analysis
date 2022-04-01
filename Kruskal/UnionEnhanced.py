import FindEnhanced as f
def unionByRank(parentList,v1,v2):
    parentV1 = f.findAbsoluteParentUnion(parentList,v1)
    parentV2 = f.findAbsoluteParentUnion(parentList,v2)
    if(parentV1.parent > parentV2.parent): 
        parentV1.parent = parentV2.vertex
        parentV2.parent -= 1
    elif(parentV1.parent < parentV2.parent): 
        parentV2.parent = parentV1.vertex
        parentV1.parent -= 1
    else:
        parentV2.parent = parentV1.vertex
        parentV1.parent -= 1
    return
