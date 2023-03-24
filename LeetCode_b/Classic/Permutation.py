# -*- coding:UTF-8 -*-
import itertools


def perm(arr, stack):
    if not arr:
        print(stack)  # 到树的最后，输出结果
        tmp = stack.copy()
        res.append(tmp)

    else:  # 没有到树的叶子节点的时候，使用递归继续往下找。
        for i in range(len(arr)):
            stack.append(arr[i])
            del arr[i]
            perm(arr, stack)
            arr.insert(i, stack.pop())


arr = [1, 2, 3]
stack = []
res = []
perm(arr, stack)
print(res)

print("^^" * 10)

def str_perm(s=''):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in str_perm(s[0:i] + s[i + 1:]):
            str_list.append(s[i] + j)
    return str_list


arr = "123"
str_list = str_perm(arr)
print(str_list)


def arr_perm(s):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in arr_perm(s[0:i] + s[i + 1:]):
            str_list.append([s[i]] + j)
    return str_list


arr = [1, 2, 3]
str_list = arr_perm(arr)
print(str_list)


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def backtrack(first=0):
        # if all integers are used up
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output

arr = [1, 2, 3]
str_list = permute(arr)
print(str_list)

print(list(itertools.permutations(arr)))

"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
"""


class Solution(object):

    def getPermutation1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        if n < 1 or k < 1:
            return None
        nums = list(range(1, n + 1))
        nums = map(str, nums)
        perm = self.permute(nums)
        for i in perm:
            ans.append("".join(list(i)))
        return ans[k - 1]

    def permute(self, nums):
        if nums is None:
            return []
        if nums == []:
            return [[]]
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        # 找到对应的n应该对应的fac坐标,就是在第一项确定的情况一下，有(n-1)!种组合
        i = n - 1
        # 构建序列，这个num是用来储存我们当前可以添加的数的，也是为避免重复
        num = list(range(1, n + 1))
        ret = ""
        while i >= 0:
            # a用来获得我们要求的那一位在num里的下标
            a, b = k // self.fac[i], k % self.fac[i]
            # 如果刚好整除干净，证明还在上一层
            if b == 0:
                a -= 1

            if a >= 0:
                ret += str(num[a])
                del num[a]
                i -= 1
            k = b
            # 如果刚好整除完，则我们已经可以知道接下来的排序情况了，它一定是最大的
            # 所以把剩下的可选的数字reverse来制造这种效果
            if b == 0:
                for i in reversed(num):
                    ret += str(i)
                break
        return ret


print("**" * 40)

n = 3
k = 3
print(Solution().getPermutation(n, k))
print(Solution().permute(list(range(1, 4))))

# print(list(itertools.permutations([1, 2, 3, 4])))
# print(list(itertools.permutations("abcd")))
