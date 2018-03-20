from bookstore.src.dao.DataAccessor import DataAccessor


class SearchEngine(DataAccessor):

    def __init__(self):
        super(SearchEngine, self).__init__()
        self.exact = '+'
        self.notMatch = '-'
        self.less = '~'
        self.all = '*'
        self.searchKeys = {}

    def matchExactWord(self, word, front=False, back=False, filterList=[]):
        if front == True or (front is True and back is True):
            query = ("select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, "
                     "available_copies, price, format, keywords, subject,image_loc "
                     "from books where title like '%{}%'").format(word)
            if len(filterList) != 0:
                inClause = ("and isbn in {}").format(tuple(filterList))
                query = ' '.join([query, inClause])
            exactmatch = super(SearchEngine, self).read(query=query)
            return self.storeSearchKeys(exactmatch, 'isbn')

        backSelector = '*' if back is True else ''
        query = (
            'select isbn, title, authors, publisher, DATE_FORMAT(yop,"%Y-%m-%d") as yop, '
            'available_copies, price, format, keywords, subject,image_loc '
            'from books where match(Title) against ("`{}`{}" in boolean mode)').format('+' + word.replace(' ', ' +'), backSelector)
        if len(filterList) != 0:
            inClause = ("and isbn in {}").format(tuple(filterList))
            query = ' '.join([query, inClause])

        exactmatch = super(SearchEngine, self).read(query=query)
        return self.storeSearchKeys(exactmatch, 'isbn')

    def matchAll(self, word, filterList=[]):
        allMatch = []
        matchedKeys = {}
        if len(word) > 3:
            for i in range(len(word), 4, -1):
                query = (
                    "select isbn, title, authors, publisher, DATE_FORMAT(yop,'%Y-%m-%d') as yop, "
                    "available_copies, price, format, keywords, subject,image_loc "
                    "from books where match(Title) against ('+{}*' in boolean mode)").format(word[:i])
                if len(filterList) != 0:
                    inClause = ("and isbn in {}").format(tuple(filterList))
                    query = ' '.join([query, inClause])

                result = super(SearchEngine, self).read(query=query)
                if len(result) > 0:
                    allMatch += result

        return self.storeSearchKeys(allMatch, 'isbn')

    def storeSearchKeys(self, searchList, key):
        result = []
        for r in searchList:
            if r.get(key) not in self.searchKeys:
                result.append(r)
            self.searchKeys[r.get(key)] = True
        return result

    def searchSingleWord(self, word, filterList=[]):
        exactMatch = self.matchExactWord(
            word, back=True, filterList=filterList)
        allMatch = self.matchAll(word, filterList=filterList)

        return exactMatch + allMatch

    def recursiveSearch(self, wordList, filterList=[]):
        result = []
        for i in range(len(wordList), 1, -1):
            for j in range(len(' '.join(wordList[:i])), 4, -1):
                word = ' '.join(wordList[:i])[:j]
                if word is not '' and len(word.strip()) is len(word):
                    exactMatch = self.matchExactWord(
                        ' '.join(wordList[:i])[:j], back=True, filterList=filterList)
                    result += exactMatch
            if len(' '.join(wordList[:i])) >= 6:
                frontOffset = len(' '.join(wordList[:i])) - 5
                for k in range(frontOffset):
                    exactMatch = self.matchExactWord(
                        ' '.join(wordList[:i])[k:], front=True, filterList=filterList)
                    result += exactMatch
        return result

    def searchMultiples(self, wordList, filterList=[]):
        allsearch = []
        exactMatch = self.matchExactWord(
            ' '.join(wordList), filterList=filterList)
        if len(exactMatch) > 0:
            allsearch += exactMatch

        allWordsSearch = self.recursiveSearch(wordList, filterList=filterList)
        if len(allWordsSearch) > 0:
            allsearch += allWordsSearch

        for i in wordList:
            allsearch += self.matchAll(i, filterList=filterList)

        return allsearch

    def searchBooks(self, query, filterList=[]):
        self.searchKeys = {}
        wordList = query.split(' ')
        wordList = list(filter(None, wordList))

        if len(wordList) == 1:
            return self.searchSingleWord(wordList[0], filterList=filterList)

        return self.searchMultiples(wordList, filterList=filterList)
