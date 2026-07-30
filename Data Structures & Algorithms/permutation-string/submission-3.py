class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        s2_count = {}
        l, r = 0, len(s1)-1
        for i in range(l, r+1):
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
        if s1_count == s2_count:
            return True

        for i in range(r+1, len(s2)):
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            if s2_count[s2[l]] > 1:
                s2_count[s2[l]] -= 1
            else:
                del s2_count[s2[l]]
            
            l += 1
            
            if s1_count == s2_count:
                return True
        return False