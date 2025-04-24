class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        map = dict()
        count = 0

        for i in nums:
            x = k - i
            if x in map and map[x] > 0: # if compliment,x is found in map 
                                        # and there is not zero key of x
                count += 1              # take a count as pair
                map[x] -= 1             # delete the x used, i is moved to the next
                                        # element
            else:
                map[i] = map.get(i, 0) + 1  # add into dictionary if not paired
        
        return count