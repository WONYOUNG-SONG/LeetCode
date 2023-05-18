class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in zip(*strs):
            tmp = set(i)
            if len(tmp) == 1:
                result += i[0]
            else:
                return result
        return result