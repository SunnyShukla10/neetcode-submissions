class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for w in strs:
            encoded_str += str(len(w)) + "#" + w
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # --> 4#neet4#code4#love3#you
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            length = int(s[i:j])
            print(length)
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j

        return res

