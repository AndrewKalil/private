#!/usr/bin/python3

def slide_window(ls=[], k=3):
    for i in range(len(ls) - k + 1):
        num = ls[i]
        for j in range(1, k):
            if ls[i + j] > num:
                num = ls[i + j]
        print(str(num) + " ", end="")

if __name__=="__main__":
    arr = [30, 35, 4, 10, -1, 67, 2, -1, -7, -10]
    k = 3
    slide_window(arr, k)