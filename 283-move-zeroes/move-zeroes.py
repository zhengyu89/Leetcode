class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Front = 0;
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[Front] = nums[i];
                Front += 1;
        for j in range(Front, len(nums)):
            nums[j] = 0;





        