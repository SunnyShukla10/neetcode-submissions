class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        # neet code loves you--> 
        for word in strs:
            encoded_str += f'{len(word)}#{word}'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        list_str = []
        idx = 0
        j = 0
        while idx < len(s):
            j = idx
            while s[j] != "#":
                j += 1
            print(s[idx:j])
            length = int(s[idx:j]) 
            print(s[j + 1 : j + length + 1])
            list_str.append(s[j + 1 : j + length + 1])
            j += length + 1
            idx = j
        return(list_str)
