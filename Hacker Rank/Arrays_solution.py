import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    
myArray = list(reversed(arr))
#print(list(reversed(myArray)))
for i in range (n):
    print(myArray[i],end=" ")