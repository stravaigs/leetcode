class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
      #int array. integer key. itll be in the array nums. "target" is number proceeding key, ie target = nums [key index + 1]. there can be many target values. need to find the one that is most frequent.
        targetlen = len(nums)//2
        targetval, targetcount = [0]*(targetlen) #at most I can have a config where every second number is the key
        for i in range (int(len(nums)-2)):
            if nums[i] == key:
                target = nums[i+1]
                for j in range(targetlen):
                    if targetval[j] == 0:
                        targetval[j] = target
                    if targetval[j] == target:
                        targetcount[j] = targetcount[j] + 1
        for k in range(targetlen):
            targetmax = 0
            if targetcount[k] > targetmax:
                targetmax = k
        return targetval[targetmax]
                
