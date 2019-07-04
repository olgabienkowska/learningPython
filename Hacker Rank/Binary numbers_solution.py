import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

binaryNumber = (bin(n))
stripped = binaryNumber.strip('0b')
noZeros = stripped.split('0')
#print(noZeros)
maxOnes = max(noZeros)
Policzone = maxOnes.count('1')
print(Policzone)