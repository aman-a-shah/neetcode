class WordDictionary:

    def __init__(self):
        # prefix tree
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for let in word:
            if let not in curr.children:
                curr.children[let] = Node()
            curr = curr.children[let]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.word == True

            if word[i] == '.':
                for child in node.children:
                    if dfs(node.children[child], i+1):
                        return True
                return False
            
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i+1)
        
        return dfs(self.root, 0)

class Node:
    def __init__(self):
        self.word = False
        self.children = {}