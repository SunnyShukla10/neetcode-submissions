class Solution:

    def encode(self, strs: List[str]) -> str:
        # Add length and then hastag before word  
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s))+"#"+s
        
        return encoded_s

    def decode(self, s: str) -> List[str]:
        # want to have a pointer that starts at the number and then go until we reach a hashtag

        #--> 5#hello5#world
        #    lr     
        res = []
        l = 0

        while l < len(s):
            r = l + 1

            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l = r+1
            res.append(s[l:l+length])
            l += length
            
        return res