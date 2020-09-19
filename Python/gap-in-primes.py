''' 
5 kyu
Gap in Primes
Link: https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4
'''

###################
# Aman's Approach #
###################

# def prime_range(m: 'int', n: 'int') -> 'list': 
    
#     temp_list = []
    
#     for j in range(m, n+1):
#         for i in range(2, (j//2 + 1)):
#             if j % i == 0: 
#                 break
#         else:
#              temp_list.append(j)


def Seieve(m, n):
    prime = [True for i in range(n+1)]
    
    p = 2
    while p*p <= n:
        
        if prime[p] == True:
            
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    c = []
    
    for p in range(m, n+1):
        if prime[p]:
            c.append(p)
    
    return c
                
    
def gap(g, m, n):
    
    pri_no_list = Seieve(m, n)
    temp_list = []
    
    for i in range(len(pri_no_list) - 1):
        if abs(pri_no_list[i] - pri_no_list[i+1]) == g:
            return [pri_no_list[i], pri_no_list[i+1]]



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
