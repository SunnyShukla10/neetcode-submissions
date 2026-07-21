class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        
        curr = self.root

        for l in word:
            if l not in curr.children:
                curr.children[l] = TrieNode()
            curr = curr.children[l]
        curr.eow = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                l = word[i]
                if l == ".":
                    # recurse
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if l not in curr.children:
                        return False
                    curr = curr.children[l]
            
            return curr.eow

        return dfs(0, self.root)


