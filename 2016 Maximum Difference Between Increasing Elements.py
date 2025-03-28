class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        # if n < 2: # deal with 1 digit array
        #     return -1
        # i = 0
        # j = 1
        # big = j   #index of the biggest number
        # small = i #index of the smallest number
        #  if nums[small] > nums[big]: #setting inital contitions, rejecting trivial case
        #      return -1


        # for j in n:
        #     if nums[j] > nums[big] and j > i:
        #         big = j
        # for i in n - 1:
        #     if nums[i] < nums[small] and i < big

        ## this approach doesn't deal with cases like [7,7,5,6,6,10,1,9] --
        # the max diff is between 1,9, but the above would stop big at 10 and take 5 as small
        # need to calculate max diff iteritively.
        #1000! not looking good though.

        maxdiff = -1

        for j in range(1, n, 1):
            # print("j: ", j)
            for i in range (0, j, 1):
                # print("looppair(i, j)", i, " ", j)
                if nums[j] - nums[i] > maxdiff:
                    maxdiff = nums[j] - nums[i]
                    # print("maxdiff: ", maxdiff)
                    # print("j: ", j)
                    # print("i: ", i)
        if maxdiff == 0:
            return -1
        return maxdiff
    


    #----------------- Optimal solution --------------------------

    # class Solution:
    # def maximumDifference(self, nums: List[int]) -> int:
    #     ans=-1
    #     low=nums[0]       
    #     for i in range(len(nums)):
    #             if low<nums[i]:
    #                 ans=max(ans,(nums[i]-low))
    #             low=min(low,nums[i])
    #     return ans
                