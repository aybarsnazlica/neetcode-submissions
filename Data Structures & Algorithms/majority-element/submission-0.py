from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for num, count in counter.items():
            if count > len(nums) // 2:
                return num

        return 0        