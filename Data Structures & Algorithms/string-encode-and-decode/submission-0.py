class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(str(len(string)) + "#" + string)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            s_len = int(s[i:j])
            result.append(s[j + 1 : j + 1 + s_len])
            i = j + 1 + s_len

        return result
