class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0   # problem description
        
        wordList.append(beginWord)
        adjList = collections.defaultdict(list)    # {pattern : [words having this pattern]}
        for word in wordList:
            for ch in range(len(word)):
                pattern = word[:ch] + '*' + word[ch + 1:]
                adjList[pattern].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1     # level

        # Go level by level and see when you reach endWord
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord: return res

                for ch in range(len(word)):
                    pattern = word[:ch] + '*' + word[ch + 1:]
                    for neighboringWord in adjList[pattern]:
                        if neighboringWord not in visited:
                            visited.add(neighboringWord)
                            queue.append(neighboringWord)

            res += 1
        
        return 0     # if no way to reach endWord