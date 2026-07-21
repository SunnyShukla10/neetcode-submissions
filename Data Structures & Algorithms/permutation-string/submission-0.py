class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])

        print(s1_count)
        print(s2_count)
        if s1_count == s2_count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)

            if s2_count[s2[l]] <= 1:
                del s2_count[s2[l]]
            else:
                s2_count[s2[l]] -= 1
            l += 1

            print(s2_count)
            print(s1_count)
            if s2_count == s1_count:
                return True 
        
        return False