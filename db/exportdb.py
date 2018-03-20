'''
Created on 21-Mar-2016

@author: parkar_s
'''
def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (len(s)!=0 and s[0] == s[len(s)-1]) and s.startswith(("'", '"'))or str(s).endswith(("'", '"')):
        return s[1:len(s)-1]
    else:
        return s
    return s
def get(arr,idx):
    for index,elem in enumerate(arr):
        if index== idx:
            return elem
    
if __name__ == '__main__':
    import os.path

    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'feedback.txt')
    filename2 = os.path.join(scriptpath, 'mongo_book.txt')
    with open(filename) as book_sql, open(filename2, "w+"):
        lines = book_sql.readlines()
        keys = ["Login_id","ISBN","Score","Date","Short_text"]
        
        documents = list()
        for line in lines:
            document = dict()
            import re
            
            line=line.replace("(","")
            line=line.replace(")","")
            line= line.replace("\n","")
            
            PATTERN = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
            arr = PATTERN.split(line)[1::2]
            
            for index,key in enumerate(keys):
                try:
                    '''if index == keys.index("Authors", ):
                        document.__setitem__(key.lower(),[dequote(arr[index])])
                    else:
                        document.__setitem__(key.lower(),dequote(arr[index]))'''
                    document.__setitem__(key.lower(),dequote(arr[index]))
                except IndexError:
                    pass
            
            documents.append(document)
        print(documents)