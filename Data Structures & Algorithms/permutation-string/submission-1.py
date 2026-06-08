from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        if len(s2)<window:
            return False
        c1 = Counter(s1)
        for i in range(0,len(s2)-window+1):
            subs = Counter(s2[i:i+window])
            if subs == c1 :
                return True
        return False