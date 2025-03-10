class Solution:
    def reverseString(self, s: List[str]) -> None:
        strlen = len(s)
        if strlen % 2 == 0:
            half = strlen//2
            for i in range(half):
                tmp = s[i]
                s[i] = s[strlen-i-1]
                s[strlen-i-1] = tmp
        else:
            half = (strlen - 1) // 2
            for i in range(half):
                tmp = s[i]
                s[i]=s[strlen-i-1]
                s[strlen-i-1] = tmp