class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, num in enumerate(nums):
            compl = target - num
            if compl in table:
                return [table[compl], i]
            
            table[num] = i

        return []