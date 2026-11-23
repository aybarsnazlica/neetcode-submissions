class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            else:
                counts[num] += 1
        
        frequencies = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            frequencies[count].append(num)
        
        result = []
        for freq in frequencies[::-1]:
            if freq:
                for n in freq:
                    result.append(n)
        
        return result[:k]
