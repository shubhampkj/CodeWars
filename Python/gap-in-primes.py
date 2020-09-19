''' 
5 kyu
Gap in Primes
Link: https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4
'''

#Aman's Approach

######################
# Shubham's Approach #
######################

#Brute Force

import math

# def isPrime(num):
#     if num%2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         if num%i == 0:
#             return False
#     return True

# def primeRange(m, n):
#     primes = []
#     for i in range(m,n+1):
#         if isPrime(i):
#             primes.append(i)
#     return primes

def primeSieve(m, n):
    sieve = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p += 1
    primes = []
    for i in range(m, n+1):
        if sieve[i]:
            primes.append(i)
    return primes
        

def gap(g, m, n):
    
    #primes = primeRange(m, n)
    primes = primeSieve(m, n)
    
    for i in range(1,len(primes)):
        prev = primes[i-1]
        curr = primes[i]
        if (curr - prev == g):
            return [prev, curr] 

#########
# Notes #
#########
