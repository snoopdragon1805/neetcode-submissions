class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        j=0
        while(j<len(strs[0])):
            temp = strs[0][j]
            for i in strs:
                if len(i)<=j or i[j] != temp:
                    return result
            result+=temp
            j+=1
        return result 