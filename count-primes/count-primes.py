'''
    Summary:-
        Sieve of Eratosthenes. Create an array of n. Mark all numbers except 0 and 1 as True.
        We start off with a table of n numbers. Let's look at the first number, 2. We know all
        multiples of 2 must not be primes, so we mark them off as non-primes. Then we look at
        the next number, 3. Similarly, all multiples of 3 such as 3 × 2 = 6, 3 × 3 = 9, ... 
        must not be primes, so we mark them off as well. Now we look at the next number, 4, 
        which was already marked off, so need to see for 4.
        
        4 is not a prime because it is divisible by 2, which means all multiples of 4 must also 
        be divisible by 2 and were already marked off. So we can skip 4 immediately and go to 
        the next number, 5. Now, all multiples of 5 such as 5 × 2 = 10, 5 × 3 = 15, 5 × 4 = 20, 
        5 × 5 = 25, ... can be marked off. There is a slight optimization here, we do not need 
        to start from 5 × 2 = 10.
        
        In fact, we can mark off multiples of 5 starting at 5 × 5 = 25, because 5 × 2 = 10 was 
        already marked off by multiple of 2, similarly 5 × 3 = 15 was already marked off by 
        multiple of 3. Therefore, if the current number is p, we can always mark off multiples 
        of p starting at p2, then in increments of p: p2 + p, p2 + 2p, ... 
        
        The terminating loop condition can be p < √n, as all non-primes ≥ √n must have already 
        been marked off. When the loop terminates, all the numbers in the table that are non-
        marked are prime.
        
        The Sieve of Eratosthenes uses an extra O(n) memory and its runtime complexity is O(n 
        log log n). 
        
        Using Multiple while or for loops in python still leads to a Time Limit Exceeded so, 
        list comprehension is used which is implemented faster in python.
        
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return 0
        
        prime = [True for i in range(n)]
        prime[1] = prime[0] = False

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                prime[i*i: n: i] = [False] * len(prime[i*i: n: i])
            
        return sum(prime)
                    
                
                