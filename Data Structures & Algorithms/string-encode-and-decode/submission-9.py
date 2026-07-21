class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for w in strs:
            s += f"{str(len(w))}#{w}"
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1            

            length = int(s[i:j])
            i = j + 1
            j = j + length + 1

            res.append(s[i:j])
            i = j    

        return res

