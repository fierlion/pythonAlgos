class Tree(object):
    def __init__(self, rootVal):
        self.root = self.Node(rootVal)

    def add(self, addVal):
        return self._add(addVal, self.root)

    def _add(self, addVal, curNode):
        if addVal > curNode.value:
            if curNode.rc is None:
                to_add = self.Node(addVal)
                curNode.rc = to_add
                return
            else:
                self._add(addVal, curNode.rc)
        elif addVal < curNode.value:
            if curNode.lc is None:
                to_add = self.Node(addVal)
                curNode.lc = to_add
                return
            else:
                self._add(addVal, curNode.lc)


    def findNext(self, rootIn):
        "find left's rightmost child, and parent of this node"
        if rootIn.lc is not None:
            cur = rootIn.lc
            while cur.rc is not None:
                par = cur
                cur = cur.rc
            par.rc = None
            return cur.value
        else:
            return rootIn

    def remove(self, remVal):
        return self._remove(remVal, self.root)

    def _remove(self, remVal, rootIn):
        # find node to remove
        # get its next
        pass

    def inOrder(self, rootIn, values=[]):
        if rootIn is not None:
            self.inOrder(rootIn.lc, values)
            values.append(str(rootIn.value))
            self.inOrder(rootIn.rc, values)
        return " ".join(values)

    class Node(object):
        def __init__(self, value=None, lc=None, rc=None):
            self.value = value
            self.lc = lc
            self.rc = rc

def makeTree():
    starterTree = Tree(50)
    #print starterTree.root.value
    starterTree.add(20)
    #print starterTree.root.lc.value
    starterTree.add(70)
    #print starterTree.root.rc.value
    starterTree.add(49)
    #print starterTree.root.lc.value
    #print starterTree.root.lc.rc.value
    starterTree.add(1001)
    print starterTree.inOrder(starterTree.root)
    print "_____"
    print starterTree.findNext(starterTree.root)

if __name__ == "__main__":
    makeTree()
