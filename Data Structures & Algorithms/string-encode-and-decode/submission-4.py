class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        # neet code loves you--> 
        for word in strs:
            encoded_str += f'{len(word)}#{word}'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        list_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            length = int(s[i:j])
            print(length)
            i = j + 1
            j = i + length

            list_str.append(s[i:j])
            i = j

        return(list_str)
