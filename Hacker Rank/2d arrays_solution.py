import math
import os
import random
import re
import sys

def funkcjaliczacasume(maciesz,i,j):
    mojaSuma = (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
    arr[i+1][j+1] +
    arr[i+2][j] + arr[i+2][j+1] + arr [i+2][j+2])
    return mojaSuma

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

mojaLista = []
mojaSuma = 0
pionowo = len(arr)
poziomo = len(arr[0])
for i in range(pionowo-2):
    for j in range(poziomo-2):
        mojaSuma = funkcjaliczacasume(arr,i, j) 
        mojaLista.append(mojaSuma)
print(max(mojaLista))

    
