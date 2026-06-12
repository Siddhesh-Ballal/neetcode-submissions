class node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: cur.children[c] = node()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root
            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in cur.children.values():
                        if dfs(j + 1, child): return True
                    return False
                else:
                    if word[j] not in cur.children: return False
                    cur = cur.children[word[j]]
            return cur.word
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)