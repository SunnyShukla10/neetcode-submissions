class TrieNode:
    def __init__(self):
        self.children = {} 
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        curr = self.root
        for l in word:
            if l not in curr.children:
                curr.children[l] = TrieNode()
            curr = curr.children[l]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        
        curr = self.root

        for l in word:
            if l not in curr.children:
                return False        
            curr = curr.children[l]
        return curr.endOfWord
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for l in prefix:
            if l not in curr.children:
                return False
            
            curr = curr.children[l]
        
        return True
        