class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i  #return latest occurance
        
        for i in range(len(nums)):
            y = target - nums[i] # find complement
            if y in h and i != h[y] :
                return [i , h[y]]
                
        return [] # no solution

# Time complexity = O(n)
# Space complexity = o(n)