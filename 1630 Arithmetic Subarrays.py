class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # say for i = 0
        # nums[l[i]] = nums[l[0]] = nums[0] = 4
        # nums[r[i]] = nums[r[0]] = nums[2] = 5
        # nums[l[i]] = 