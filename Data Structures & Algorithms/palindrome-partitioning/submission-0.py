class Solution:
    def is_pallindrome(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(i): 
            if i == len(s):
                res.append(partition[:])
                return
            
            for j in range(i, len(s)):
                if self.is_pallindrome(s[i : j + 1]):
                    partition.append(s[i : j + 1])
                    backtrack(j + 1)
                    partition.pop()
            
        backtrack(0)

        return res