class Solution(object):
    def countOdds(self, low, high):
        count = 0
        if low == high:
            if low % 2 == 0:
                count = 0
            else:
                count = 1
            return count
        if low % 2 == 0:
…                if skip > high:
                    break
            return count



        
