class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        curr = self.root

        for l in word:
            if l not in curr.children:
                curr.children[l] = TrieNode()
            curr = curr.children[l] 
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            curr = node
            
            for i in range(j, len(word)):
                if word[i] == ".":
                    for childNode in curr.children.values():
                        if dfs(childNode, i+1):
                            return True
                    return False
            
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.endOfWord

        return dfs(self.root, 0)