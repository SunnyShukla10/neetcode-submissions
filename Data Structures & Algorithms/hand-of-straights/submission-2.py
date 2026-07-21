class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:        
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        heap = list(freq.keys())

        heapq.heapify(heap)
        
        while heap:
            min_val = heap[0]
            
            # iterate from min_val to min_val+groupsize
            for i in range(min_val, min_val + groupSize):
                if i not in freq:
                    return False
                
                freq[i] -= 1

                if freq[i] == 0:
                    if i != heap[0]:
                        return False # we are creating a hole 
                    heapq.heappop(heap)
        return True
            
        
