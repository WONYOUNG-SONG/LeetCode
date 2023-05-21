class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(format(int(a, 2) + int(b, 2), 'b'))