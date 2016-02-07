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

def isBalanced(treeIn):
    result = getMaxDepth(treeIn.root, 0)
    return True if result > -1 else False

def getMaxDepth(rootNode, depth):
    if rootNode is None:
        return 0
    ldepth = getMaxDepth(rootNode.lc, depth)
    rdepth = getMaxDepth(rootNode.rc, depth)
    if ldepth == -1 or rdepth == -1:
        return -1
    if abs(ldepth - rdepth) > 1:
        return -1
    max_depth = max(ldepth+1, rdepth+1)
    print rootNode.value, ldepth, rdepth, max_depth
    return max_depth

def makeTrees():
    starterTree = Tree(50)
    start_add = [20, 70, 49, 1001]
    for s_add in start_add:
        starterTree.add(s_add)
    print "starterTree inOrder: " + starterTree.inOrder()
    balancedTree = Tree(5)
    test_add = [1,9]
    for t_add in test_add:
        balancedTree.add(t_add)
    unbalancedTree = Tree(5)
    test_add += [2,3]
    for t_add in test_add:
        unbalancedTree.add(t_add)
    print "balancedTree inOrder: " + balancedTree.inOrder()
    print "unbalancedTree inOrder: " + unbalancedTree.inOrder()
    print isBalanced(balancedTree)
    print isBalanced(unbalancedTree)

if __name__ == "__main__":
    makeTrees()
