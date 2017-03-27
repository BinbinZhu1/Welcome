# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:24:45 2017

@author: welcome
"""

def factorial(x):
    result=x
    for i in range(1,x):
        result*=i
    return result        

print factorial(6)


# 递归实现阶乘

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print factorial(7)


def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1) # An example of recursion

#binary search
def search(seq,number,lower=0,upper=None):
    if upper is None:
        upper=len(seq)-1
    if lower==upper:
        assert number==seq[upper] #断言所查找的数字一定会被找到
        return upper
    else:
        middle=(lower+upper)/2
        if number>seq[middle]:
            return search(seq,number,middle+1,upper)
        else:
            return search(seq,number,lower,middle)
seq=[22, 23, 1, 3, 8, 99, 34,99,22, 24, 341, 32, 41, 214, 12341]       
seq.sort()
print search(seq,341)
