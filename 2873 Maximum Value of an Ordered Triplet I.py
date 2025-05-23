import math

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        tripletmax = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1, 1):
                for k in range(j + 1, len(nums), 1):
                    tripletcalc = (nums[i] - nums[j]) * nums[k]
                    if tripletcalc > tripletmax:
                        tripletmax=tripletcalc
        return tripletmax