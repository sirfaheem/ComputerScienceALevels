class nodeLister(object):
    def __init__(self,d,p):
        self.data = d
        self.ptr = p
    def dSetter(self,d):
        self.data = d
    def pSetter(self,p):
        self.ptr = p
    def pGetter(self):
        return self.ptr
    def dGetter(self):
        return self.data

class listConstructor(object):

    def initList(self,n,nodes):
        self.starPtr = n
        self.freePtr = 1
        for i in range(1,7):
            x = i+1
            nodes[i].pSetter(x)
        nodes[7].pSetter(n)

    def main(self):
        nullPtr = 0
        nodes = [0]
        
        for i in range(1,8):
            nodes.append(i)
            
            nodes[i] = nodeLister(0,0)

        self.initList(nullPtr,nodes)

        for i in range(1,8):
            print(nodes[i].pGetter(),nodes[i].dGetter())

    
        
x = listConstructor()
x.main()
