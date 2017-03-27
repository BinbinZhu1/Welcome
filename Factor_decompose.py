# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:55:05 2017

@author: welcome
"""

#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.
#编程找出1000以内的所有完数。

   
def Factor(n):
    if not isinstance(n,int) or n<0:
        print "Data error!"
    elif n==1:
        print "{}".format(n),
    factor=[1]
    for i in range(2,n):
        if n%i==0:
            factor.append(i)
    return factor
    
            
for n in range(2,1001):
    factor=Factor(n)
    if n==reduce(lambda x,y:x+y,factor):
        print n
        print factor
#质因数分解
def decompos(n):

    if not isinstance(n,int) or n<0:
        print "Data error!"
    elif n==1:
        print '{}'.format(n),
    prime=[1]
    while n!=1:
        for i in xrange(2,n+1):
            if n % i==0:
                n=n/i
                if n==1:
                    prime.append(i)  
                else:
                    prime.append(i)
                break 
    return prime
        
        
    
if __name__=="__main__":
    print "Hello!"
