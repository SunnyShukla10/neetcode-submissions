class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        PHONE_MAP = {"2": "abc", "3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}
        res = []
        subset = []

        def backtrack(i):
            if i == len(digits):
                print(subset)
                res.append("".join(subset))
                return
                    
            digit = digits[i]
            letters = PHONE_MAP[digit]
            
            for letter in letters:
                subset.append(letter)
                backtrack(i+1)
                subset.pop()
            
        backtrack(0)
        return res if digits else []