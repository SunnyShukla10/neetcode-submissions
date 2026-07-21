class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:        
        if len(hand) % groupSize != 0:
            return False

        max_val = max(hand)
        freq = Counter(hand)

        while freq:
            min_val = min(freq)
            i = 0

            while i < groupSize:
                print(min_val)

                if min_val not in freq:
                    return False
                
                i += 1

                if freq[min_val] == 1:
                    freq.pop(min_val)
                else:
                    freq[min_val] -= 1
                
                min_val += 1

                print(freq)

        return True
            
        
