class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
        for k,v in counter.items():
            if v > 1:
                return True
        
        return False