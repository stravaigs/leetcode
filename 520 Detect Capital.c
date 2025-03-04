#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

//Single char case, all lower case, upper case then lower case, all upper case.
bool detectCapitalUse(char* word) {
    int n = strlen(word);
    int count = 0;
    if (n == 1)
    {
        return true;
    }
    if (islower(word[0]))
    {
        for (int i = 1; i < n; i++)
        {
            if (islower(word[i])) 
            {
                count++;
            }
            if (count == n - 1)
            {
                return true;
            }
        }
    }
    if (isupper(word[0]))
    {
        for (int i = 1; i < n; i++)
        {
            if (islower(word[i]))
            {
                count++;
            }
            if (count == n - 1)
            {
                return true;
            }
        }
        count = 0;
        for (int i = 1; i < n; i++)
        {
            if (isupper(word[i]))
            {
                count++;
            }
            if (count == n - 1)
            {
                return true;
            }
        }
    }
    return false; 
}