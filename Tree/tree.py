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

    def inOrder(self):
        empty = []
        startRoot = self.root
        return self._inOrder(startRoot, empty)

    def _inOrder(self, rootIn, values):
        if rootIn is not None:
            self._inOrder(rootIn.lc, values)
            values.append(str(rootIn.value))
            self._inOrder(rootIn.rc, values)
        return " ".join(values)

    class Node(object):
        def __init__(self, value=None, lc=None, rc=None):
            self.value = value
            self.lc = lc
            self.rc = rc

def makeTrees():
    starterTree = Tree(50)
    start_add = [20, 70, 49, 1001]
    for s_add in start_add:
        starterTree.add(s_add)
    print "starterTree inOrder: " + starterTree.inOrder()
    balancedTree = Tree(5)
    test_add = [3,1,9]
    for t_add in test_add:
        balancedTree.add(t_add)
    unbalancedTree = Tree(5)
    test_add += [2]
    for t_add in test_add:
        unbalancedTree.add(t_add)
    print "balancedTree inOrder: " + balancedTree.inOrder()
    print "unbalancedTree inOrder: " + unbalancedTree.inOrder()

if __name__ == "__main__":
    makeTrees()
