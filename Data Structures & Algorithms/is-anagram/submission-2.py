class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Count1={}
        Count2={}
        for char in s:
            Count1[char] = Count1.get(char,0)+1
        for char in t:
            Count2[char] = Count2.get(char,0)+1
        if Count1 == Count2:
            return True
        return False
        