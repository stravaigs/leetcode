class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bubble sort this - max 300 vals
        swap = 0
        noswap = 1
        while noswap == 1:
            noswap = 0
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    swap = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = swap
                    noswap = 1
