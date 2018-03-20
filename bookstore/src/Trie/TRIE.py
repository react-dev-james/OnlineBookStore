'''
Created on Jun 17, 2016

@author: Dell
'''
from _collections import defaultdict


class TRIE():

    def __init__(self):
        self.root = defaultdict()

    def rawInsert(self, word, end=None):
        current = self.root
        for i, v in enumerate(word):
            if v in current:
                current = current[v]
            else:
                current[v] = {}
                current = current[v]
        current.setdefault('__end__')
        if end is not None:
            current.setdefault('__id__', end)
        current.setdefault('frequency', 0)
        current['frequency'] = current['frequency'] + 1

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault('_end')
        current.setdefault('frequency', 0)
        current['frequency'] = current['frequency'] + 1

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if '_end' in current:
            return True
        return False

    def getFrequncies(self, node):
        for wordStart in node:
            if wordStart == '_end':
                print(node['frequency'])
            else:
                if wordStart != 'frequency':
                    self.getFrequncies(node[wordStart])

    def add(self, word):
        current = self.root
        for char in word:
            current = current.setdefault(char, {})
        current.setdefault('_end')

    def findFrequency(self, para):
        word = ''
        for char in para:
            if char.isspace():
                self.rawInsert(word)
                word = ''
            else:
                word += char
        self.insert(word)
        self.getFrequncies(self.root)

    def insertUtil(self, minHeap, word, duplicate):
        if self.root == None:
            self.root = defaultdict()
