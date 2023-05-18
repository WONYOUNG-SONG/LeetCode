class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,"D": 500, "M": 1000}       
        
        return sum(map(lambda x: Roman_dic[x], s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")))