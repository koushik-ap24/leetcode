## Classic Trie problem
## Need to recurse if "." otherwise do standard trie prefix search.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class WordDictionary:
    def __init__(self):
       self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endofWord = True

    def search(self, word: str) -> bool:
        # If "." the recurse through all children until a match is found.
        def recurse(start, curr):
            for i in range(start, len(word)):
                c = word[i]
                if c == ".":
                    for letter, node in curr.children.items():
                        if recurse(i + 1, node):
                            return True
                    return False
                elif c not in curr.children:
                    return False
                curr = curr.children[c]

            return curr.endofWord

        return recurse(0, self.root)