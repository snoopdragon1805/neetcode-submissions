class Solution:
    def buildDict(self, s):
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        return freq

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = []
        for i in range(len(strs)):
            if strs[i] in seen:
                continue
            temp = [strs[i]]
            if i == len(strs)-1:
                result.append(temp)
                break
            freq_i = self.buildDict(strs[i])
            for j in range(i+1,len(strs)):
                freq_j = self.buildDict(strs[j])
                if freq_i == freq_j:
                    temp.append(strs[j])
                    seen.append(strs[j])
            result.append(temp)
        return result




            
            
        