# -*- coding:UTF-8 -*-


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return 0
        num_of_2, num_of_5 = self.process(n - 1)
        while n and (n % 2 == 0 or n % 5 == 0):
            if n % 2 == 0:
                num_of_2 += 1
                n >>= 1
            if n % 5 == 0:
                num_of_5 += 1
                n //= 5
        return min(num_of_2, num_of_5)

    def process(self, n):
        if n == 1:
            return 0, 0
        num_of_2, num_of_5 = self.process(n - 1)
        while n and (n % 2 == 0 or n % 5 == 0):
            if n % 2 == 0:
                num_of_2 += 1
                n >>= 1
            if n % 5 == 0:
                num_of_5 += 1
                n //= 5
        return num_of_2, num_of_5

    def trailingZeroes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return 0
        num_of_5 = 0
        for i in range(1, n + 1):
            while i and i % 5 == 0:
                if i % 5 == 0:
                    num_of_5 += 1
                    i //= 5
        return num_of_5

    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def f(n):
            res = 0
            while n > 0:
                res += n // 5
                n //= 5
            return res

        low, up = 0, 5 * 10 ** 9
        while up > low + 1:
            mid = (low + up) // 2
            tmp = f(mid)
            if K == tmp: return 5
            if K > tmp: low = mid
            if K < tmp: up = mid
        return 0


if __name__ == '__main__':
    print(Solution().trailingZeroes1(25))
    print(Solution().preimageSizeFZF(5))
