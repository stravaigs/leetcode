#include <stdio.h>
#include <math.h>

int largestInteger(int num) {
    //I want to index into num and then sort highest to lowest and return the number
    //To index first we need to count length.
    int *numarray = NULL;
    int count = 0;
    int i, key;
    while (num > 0)
    {
        count++;
        numarray = (int *)realloc(numarray, count * sizeof(int));
        if (numarray == NULL) // fail to allocate memory
        {
            return 1;
        }
        numarray[count - 1] = log10((int)num); // place the number at the end of the array
        key = numarray[count - 1];
        if (count > 1) // insertion sort, need to compare 2 values first instert is trivial
        {
            for (i = 0; i < count - 2; i++)
            {
                if (log2(key) == log2(numarray[count - i - 2]) && key > numarray[count - i - 2])//if the key and the number to it's right are both even or odd, while the current number (key) just insterted is greater than the one to it's right
                {
                    numarray[count - i - 1] = numarray[count - i - 2]; //swap the value to the right with key value
                    numarray[count - i - 2] = key;
                }
            }
        }
        num /= 10;
    
    }
    num = 0;
    for (int j = 0; j < (count - 1); j++)
    {
        num = num + numarray[j] * 10 ^ (count - 1 - j);
    }
    free(numarray);
    return num;
}