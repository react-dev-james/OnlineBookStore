from bookstore.src.models.core.business.tree import Tree


class Category(object):

    def __init__(self, name, i):
        self.id = i
        self.name = name

    def __str__(self):
        return str(self.id) + ' ' + self.name

    def __repr__(self):
        return str(self.id) + ' ' + self.name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
