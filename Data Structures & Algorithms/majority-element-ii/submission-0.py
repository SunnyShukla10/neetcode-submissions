class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # First declare the counter dict  
        count = defaultdict(int)
        majority_freq = len(nums) // 3
        res = []
        for num in nums:
            count[num] += 1

            if len(count) > 2:
                # decrement the counts of each key
                new_count = defaultdict(int)

                for key, val in count.items():
                    if val > 1:
                        new_count[key] = (val - 1)
                count = new_count

        for key in count.keys():
            actual_count = nums.count(key)
            if actual_count > majority_freq:
                res.append(key)

        return res
