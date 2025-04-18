class Solution:
    def clearDigits(self, s: str) -> str:
        length = len(s)
        print("length: ", length)
        kmax = 0
        i = 1
        while i < length:
            print("i: ", i)
            if s[i].isdigit():
                print("s[i] if digit: ", s[i])
                for j in range(0, i):
                    if s[j].isalpha():
                        s = s[:i] + s[i+1:] # delete digit
                        length = length - 1
                    for k in range(0, i):
                        if s[k].isalpha():
                            kmax = k
                    s = s[:kmax] + s[kmax+1:]
                    length = length - 1
            i += 1
        return s


## working solution, with help below##

    # class Solution:
    #     def clearDigits(self, s: str) -> str:
    #         length = len(s)
    #         print("length: ", length)
    #         i = 1
    #         while i < length:
    #             print("i: ", i)
    #             if s[i].isdigit():
    #                 print("s[i] if digit: ", s[i])
    #                 has_letter = False
    #                 for j in range(0, i):
    #                     if s[j].isalpha():
    #                         has_letter = True
    #                         break
    #                 if has_letter:
    #                     s = s[:i] + s[i+1:] # delete digit
    #                     length = length - 1
    #                     kmax = -1  # properly reset kmax
    #                     for k in range(0, i):
    #                         if s[k].isalpha():
    #                             kmax = k
    #                     s = s[:kmax] + s[kmax+1:]
    #                     length = length - 1
    #                     i = 0  # restart from beginning since string changed
    #             i += 1
    #         return s


