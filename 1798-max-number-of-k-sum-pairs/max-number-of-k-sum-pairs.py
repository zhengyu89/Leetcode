class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # making hash map
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        maxOperations = 0
    
        for num in list(freq.keys()):
            complement = k - num
            if complement in freq:
                if num == complement:
                    pairs = freq[num] // 2
                else:
                    pairs = min(freq[num], freq[complement])
                
                maxOperations += pairs
                freq[num] -= pairs
                freq[complement] -= pairs

        return maxOperations