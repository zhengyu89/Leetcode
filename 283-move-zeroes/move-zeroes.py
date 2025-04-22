class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        NumberOfZeros= 0;
        TempList = [];

        for i in range(len(nums)):
            if nums[i] == 0:
                NumberOfZeros += 1;
            else:
                TempList.append(nums[i]);

        for j in range(NumberOfZeros):
            TempList.append(0);
        
        for k in range(len(nums)):
            nums[k] = TempList[k]


        