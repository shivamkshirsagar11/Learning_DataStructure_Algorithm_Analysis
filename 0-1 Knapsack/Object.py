class Object: 
    profit = 0
    weight = 0
    def __init__(self,p,w):
        self.profit = p
        self.weight = w
def MakeObjects():
    ObjArray = []
    ObjArray.append(Object(60,10))
    ObjArray.append(Object(100,20))
    ObjArray.append(Object(120,30))
    # ObjArray.append(Object(45,9))
    # ObjArray.append(Object(37,4))
    return ObjArray