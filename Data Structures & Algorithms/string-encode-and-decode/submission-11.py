class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"
        
        return encoded_str

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        while i < len(s):
            # get to hashtag
            j = i
            while s[j] != "#":
                j+=1

            length = int(s[i:j])

            word = s[j+1:j+1+length]
            res.append(word)
            
            j = j + 1 + length 
            i = j
        return res