class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxcount = -1
        # print("lens: ", len(s))
        if len(s) == 0 or len(s) == 1: # for empty, length 1 arrays. lol if len(s) == 0 or 1: =/= if len(s) == 0 or len(s) == 1:
            return maxcount
        for i in range(0, len(s)): # loop through the array
            # print("i: ", i)
            for j in range(i+1,len(s)): # loop from one point after where we are in the array + 1 to the end
                # tempcount = j-i-1
                # print("j: ", j)
                # print("i: ", i)
                # print("j-i-1", tempcount)

                if s[i] == s[j] and j-i-1 > maxcount:
                    maxcount = j-i-1
        return maxcount    