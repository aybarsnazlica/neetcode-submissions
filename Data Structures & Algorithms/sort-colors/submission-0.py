class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for num in nums:
            counter[num] += 1

        start = 0
        for color, count in enumerate(counter):
            for i in range(start, start + count):
                nums[i] = color
            start += count
