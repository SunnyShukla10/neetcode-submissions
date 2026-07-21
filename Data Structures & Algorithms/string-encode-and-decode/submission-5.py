class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for w in strs:
            encoded_str += str(len(w)) + "#" + w
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            str_len = int(s[i:j])

            i = j + 1
            j = i + str_len
            word = s[i:j]
            res.append(word)
            i = j
        
        return res