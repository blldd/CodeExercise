# -*- coding:UTF-8 -*-
"""
The ... file.

Authors: dedong (ddlecnu@gmail.com)
"""


def sum_2(arr, target):
    hash_table = {}
    res = []
    for i in range(len(arr)):
        if target - arr[i] in hash_table:
            res.append([hash_table[target - arr[i]], i])
        hash_table[arr[i]] = i
    return res


def sum_3(arr, target):
    arr.sort()
    len1 = len(arr)
    res = []
    if len1 < 3:
        print(res)
    for i in range(len1 - 1):
        left, right = i + 1, len1 - 1  # 以下思路与2sum中的快速排序思想一样
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == target and [arr[i], arr[left], arr[right]] not in res:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1
    print(res)


def sum_3_2(arr, target):  # 3sum问题 解 2
    res = []
    for i, value1 in enumerate(arr):
        for j, value2 in enumerate(arr[i + 1:]):
            if (target - value1 - value2) in arr[i + 2:]:
                minV = min(value1, value2, target - value1 - value2)
                maxV = max(value1, value2, target - value1 - value2)
                midV = target - minV - maxV
                res.append((minV, midV, maxV))
    print(list(set(res)))


def continuous_pos_sum(target):
    res = []
    if target < 1:
        return
    small = 1
    big = 2
    cur_sum = small + big
    mid = (1 + target) / 2
    while small < mid:
        if cur_sum < target:
            big += 1
            cur_sum += big
        elif cur_sum > target:
            cur_sum -= small
            small += 1
        else:
            res.append([i for i in range(small, big + 1)])
            cur_sum -= small
            small += 1
    return res


def combinationSum(candidates, target):
    """
    不限次数
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def helper(remain, combi, idx):
        if remain < 0:
            return
        if remain == 0:
            res.append(combi)
            return
        if idx >= len(candidates):
            return
        helper(remain, combi, idx + 1)
        helper(remain - candidates[idx], combi + [candidates[idx]], idx)

    res = []
    helper(target, [], 0)
    return res


def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def helper(remain, combi, idx):
        if remain < 0:
            return
        if remain == 0 and combi not in res:
            res.append(combi)
            return
        if idx >= len(candidates):
            return
        helper(remain, combi, idx + 1)
        helper(remain - candidates[idx], combi + [candidates[idx]], idx + 1)

    res = []
    candidates.sort()
    helper(target, [], 0)
    return res


class Solution:
    """
    leetcode 40
    给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

    candidates 中的每个数字在每个组合中只能使用一次。
    """

    def combinationSum2(self, candidates, target):
        # 下面有一个目标值小于某一元素就break，所以先排序
        candidates.sort()
        # 储存返回的二维列表
        res, length = [], len(candidates)

        # 递归，目标值，起始位置，当前组合
        def dfs(target, start, vlist):
            # 目标值为0，表明当前递归完成，把当前递归结果加入res并返回
            if target == 0:
                return res.append(vlist)
            # 从开始下标循环
            for i in range(start, length):
                # candidates有序，只要当前大于目标后面都大于，直接break
                if target < candidates[i]:
                    break
                # 这个判断保证不重复例如1，1，2，5，6，7，10，第二个1就会被跳过
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # 否则目标值减当前值，i+1为新的起始位置（不用重复数字），把当前值加入当前组合
                else:
                    dfs(target - candidates[i], i + 1, vlist + [candidates[i]])

        dfs(target, 0, [])
        return res

    """
    leetcode 39
    给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

    candidates 中的每个数字在每个组合中次数不限。
    """

    def combinationSum(self, candidates, target):
        # 下面有一个目标值小于某一元素就break，所以先排序
        candidates.sort()
        # 储存返回的二维列表
        res, length = [], len(candidates)

        # 递归，目标值，起始位置，当前组合
        def dfs(target, start, vlist):
            # 目标值为0，表明当前递归完成，把当前递归结果加入res并返回
            if target == 0:
                return res.append(vlist)
            # 从开始下标循环
            for i in range(start, length):
                # candidates有序，只要当前大于目标后面都大于，直接break
                if target < candidates[i]: break
                # 这个判断保证不重复例如1，1，2，5，6，7，10，第二个1就会被跳过
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # 否则目标值减当前值，i为用重复数字，把当前值加入当前组合
                else:
                    dfs(target - candidates[i], i, vlist + [candidates[i]])

        dfs(target, 0, [])
        return res


if __name__ == '__main__':
    nums = [1, 4, 3, 2, 6, 5]
    target = 6

    print(sum_2(nums, target))
    sum_3(nums, target)
    sum_3_2(nums, target)

    print(continuous_pos_sum(15))

    print(combinationSum([2, 3, 6, 7], 7))
    print(combinationSum2([2, 3, 6, 7], 7))

    # print(Solution().combinationSum2([2, 3, 6, 7], 7))
    print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))  # 提交时请删除该行
    print(Solution().combinationSum(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))  # 提交时请删除该行
