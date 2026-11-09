class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_array = [0] * 26
        for i in range(len(s)):
            freq_array[ord(s[i]) - ord("a")] += 1
            freq_array[ord(t[i]) - ord("a")] -= 1
            
        for i in freq_array:
            if i != 0:
                return False
        
        return True