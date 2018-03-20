

class Node():

    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data) + str(self.children)


class Tree(object):
    _instance = None

    def __init__(self, root):
        self.root = Node(root)

    def find(self, data):
        return self.__find__(self.root, data)

    def add(self, data, parent):
        if parent == self.root.data:
            self.root.children.append(Node(data))
            return True
        if data is not self.root.data:
            parentNode = self.find(parent)
            if parentNode is not None:
                parentNode.children.append(Node(data))
                return True

    def getChildren(self, node, childrenList):

        for i in node.children:
            childrenList.append(i.data.id)
            self.getChildren(i, childrenList)

    def getAllChildren(self, data):
        node = self.find(data)
        childrenList = []
        if node is not None:
            self.getChildren(node, childrenList)

        return childrenList

    def __find__(self, node, data):
        result = None
        if node.data == data:
            return node
        else:
            for i in node.children:
                result = self.__find__(i, data)
                if result is not None:
                    return result
            return result
