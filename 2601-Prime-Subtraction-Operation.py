from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            if n < 2:
                return False

            for f in range(2, int(n ** .5) + 1):
                if n % f == 0:
                    return False
            return True

        primes = [0]
        for i in range(1,max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i-1])
        prev = 0
        print(primes)
        for n in nums:
            upper = n - prev
            largets_prime = primes[upper - 1]
            if n - largets_prime <= prev:
                return False
            prev = n - largets_prime
        return True