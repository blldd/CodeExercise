# -*- coding:UTF-8 -*-

'''
Count the number of prime numbers less than a non-negative number, n.
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1:
            return 0

        isPrime = [True] * (n+1)
        isPrime[0], isPrime[1] = False, False

        for i in range(2, n):
            if i * i > n:
                break

            if isPrime[i] == False:
                continue

            j = i*i
            while j <= n:
                isPrime[j]=False
                j+=i


        # count
        c = 0
        for i in range(n):
            if isPrime[i]:
                c += 1
        return c



if __name__ == '__main__':
    print(Solution().countPrimes(10))
