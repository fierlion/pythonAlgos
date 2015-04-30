# bunch pattern by Alex Martelli from "the python cookbook"

class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self

ray = Bunch(name="Ray Allan", position="Programmer")
print("ray position: "+ ray.position) 

Tree = Bunch
tree = Tree(left=Tree(left="a", right="b"), right=Tree(left="c"))
print("tree left: " + str(tree.left))
print("tree left-right: " + str(tree.left.right))