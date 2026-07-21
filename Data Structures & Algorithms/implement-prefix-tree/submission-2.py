class TrieNode:
    def __init__(self):
        self.children = {} # letter : TrieNode
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
        node.endOfWord = True
    
    def search(self, word: str) -> bool:
        node = self.root

        for l in word:
            if l not in node.children:
                return False    
            node = node.children[l]
        
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for l in prefix:
            if l not in node.children:
                return False
            
            node = node.children[l]
        
        return True


        