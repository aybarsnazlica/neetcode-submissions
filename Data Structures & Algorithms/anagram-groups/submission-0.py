from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            freq_arr = [0] * 26
            
            for letter in s:
                freq_arr[ord(letter) - ord('a')] += 1
            
            groups[tuple(freq_arr)].append(s)

        return list(groups.values())
