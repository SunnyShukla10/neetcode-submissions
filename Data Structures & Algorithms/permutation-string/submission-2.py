class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        d2 = Counter(s2[:len(s1)])

        if d1 == d2:
            return True

        l = 0
        for i in range(len(s1), len(s2)):
            print(d1, d2)
    
            if d2[s2[l]] > 1:
                d2[s2[l]] -= 1
            else:
                del d2[s2[l]]

            d2[s2[i]] = d2.get(s2[i], 0) + 1

            if d1 == d2:
                return True
            l+=1
        return False