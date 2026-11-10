class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i, num in enumerate(nums):
            indexes[num] = i

        for i, num in enumerate(nums):
            compl = target - num
            if compl in indexes and indexes[compl] != i:
                return [i, indexes[compl]]
        
        return []