class Solution:
    # we can encode the string with a number and one character
    # we will put each word like {num}{char}{word} so for ex) --> ["Hello","World"] : 5#Hello5#World --> turn back into the orig
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        r = 0
        # 5#Hello5#World
        # lr 
        while r < len(s):
            l = r
            
            while s[r] != "#":
                r += 1
            
            length = int(s[l:r])
            l = r+1
            word = s[l:l+length]
            res.append(word)

            r = l+length
        return res