#Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

#There may be duplicates in the original array.

#Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        b = [0]*l
        x = 0 # rotation point
        for i in range (1, l):
            if nums[i] < nums[i-1]:
                x = i #updated rotation point, and where we want to start b
        for j in range (l):
            b[j] = nums[(j+x) % l]
        for j in range (1, l):
            if b[j-1] > b[j]: #it will return false if out of order, but if all correct will return true
                return False
        return True
