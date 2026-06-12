class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone_map = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        }

        res = []

        def dfs(i, combination):
            if i == len(digits):
                res.append(combination)
                return
            
            for letter in phone_map[digits[i]]:
                dfs(i + 1, combination + letter)
        
        dfs(0, "")

        return res