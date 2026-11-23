class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        frequencies = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            frequencies[count].append(num)

        result = []
        for freq in frequencies[::-1]:
            if freq:
                for num in freq:
                    result.append(num)
                    if len(result) == k:
                        return result

        return []
