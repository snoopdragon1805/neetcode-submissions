class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        count = 0
        prefix=0
        for num in nums:
            prefix+=num

            if prefix-k in freq:
                count+=freq[prefix-k]
            freq[prefix] = freq.get(prefix,0)+1
        return count