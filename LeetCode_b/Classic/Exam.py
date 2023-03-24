import collections
import sys
import numpy as np
import itertools as it

import sys

if __name__ == "__main__":
    pass
    # # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     for v in values:
    #         ans += v
    # print(ans)

"""
堆排序
"""


def down_adjust_min(array, parentIndex, length):
    temp = array[parentIndex]
    childIndex = 2 * parentIndex + 1
    while (childIndex < length):
        if childIndex + 1 < length and array[childIndex + 1] < array[childIndex]:
            childIndex += 1
        if temp <= array[childIndex]:
            break
        array[parentIndex] = array[childIndex]
        parentIndex = childIndex
        childIndex = 2 * childIndex + 1
    array[parentIndex] = temp


def heap_sort(array):
    """
    堆排序算法的步骤：
    1. 把无序数组构建成二叉堆。
    2. 循环删除堆顶元素，移到集合尾部，调节堆产生新的堆顶。
    :param array:
    :return:
    """
    # 1.构建二叉堆
    for i in range(int(len(array) / 2))[::-1]:
        down_adjust_min(array, i, len(array))
    print(array)

    # 2.循环删除堆顶元素，移到集合尾部，调节堆产生新的堆顶
    for i in range(len(array))[::-1]:
        array[i], array[0] = array[0], array[i]
        down_adjust_min(array, 0, i)
    print(array)


"""
快排
"""


def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] >= key:
            right -= 1
        array[left], array[right] = array[right], array[left]
        while left < right and array[left] <= key:
            left += 1
        array[right], array[left] = array[left], array[right]
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


quick_sort_lam = lambda array: array if len(array) <= 1 else \
    quick_sort_lam([item for item in array[1:] if item <= array[0]]) \
    + [array[0]] + \
    quick_sort_lam([item for item in array[1:] if item > array[0]])

"""

"""


def quick_sort_stack(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])


def bubble_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    for i in range(length)[::-1]:
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 广度优先遍历算法
def level_queue(root):
    if root is None:
        return
    my_queue = collections.deque()
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.popleft()
        print(node.val)
        if node.left is not None:
            my_queue.append(node.left)
        if node.right is not None:
            my_queue.append(node.right)


# 深度优先遍历算法
def depth_tree(tree_node):
    if tree_node is not None:
        print(tree_node.val)
        if tree_node.left is not None:
            depth_tree(tree_node.left)
        if tree_node.right is not None:
            depth_tree(tree_node.right)


def postorderTraversal_recur(root):  ##后序遍历
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    return postorderTraversal_recur(root.left) + postorderTraversal_recur(root.right) + [root.val]


"""
当前结点curr不为None时，每一次循环将当前结点curr入栈；
当前结点curr为None时，则出栈一个结点，且打印出栈结点的value值。
整个循环在stack和curr皆为None的时候结束。
"""


def inorderTraversal(root):
    stack = []
    res = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
    return res


"""
由于前序遍历的顺序是中左右，所以我们每次先打印当前结点curr，并将右子结点push到栈中，然后将左子结点设为当前结点。
入栈和出栈条件（当前结点curr不为None时，每一次循环将当前结点curr入栈；
当前结点curr为None时，则出栈一个结点）以及循环结束条件
（整个循环在stack和curr皆为None的时候结束）与中序遍历一模一样。
"""


def preorderTraversal(root):  ## 前序遍历
    stack = []
    res = []
    curr = root
    while stack or curr:
        if curr:
            res.append(curr.val)
            stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()
    return res


"""
代码的主体部分基本就是.right和.left交换了顺序，
且后序遍历在最后输出的时候进行了反向（因为要从 中右左 变为 左右中 ）
"""


def postorderTraversal(root):  ## 后序遍历
    stack = []
    res = []
    curr = root
    while stack or curr:
        if curr:
            res.append(curr.val)
            stack.append(curr.left)
            curr = curr.right
        else:
            curr = stack.pop()
    return res[::-1]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序 中序 构建树
def getTreePreMid(pre, mid):
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    root = TreeNode(pre[0])
    root_index = mid.index(pre[0])
    root.left = getTreePreMid(pre[1:root_index + 1], mid[:root_index])
    root.right = getTreePreMid(pre[root_index + 1:], mid[root_index + 1:])
    return root


"""
动态规划
"""


def palindrome_seq(s):
    """
    给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长
    :return:
    """
    length = len(s)
    if length < 2:
        return 0
    rs = s[::-1]
    dp = [[0 for i in range(length + 1)] for j in range(length + 1)]
    for i in range(1, length + 1):
        for j in range(1, length + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if s[i - 1] == rs[j - 1] else max(dp[i][j - 1], dp[i - 1][j])
    for i in dp:
        print(i)
    return length - dp[length][length]


# 编辑距离
def levenshtein_distance_dp(input_x, input_y):
    xlen = len(input_x) + 1
    ylen = len(input_y) + 1

    # 此处需要多开辟一个元素存储最后一轮的计算结果
    dp = [[0 for i in range(xlen)] for j in range(ylen)]
    for i in range(xlen):
        dp[i][0] = i
    for j in range(ylen):
        dp[0][j] = j

    for i in range(1, xlen):
        for j in range(1, ylen):
            if input_x[i - 1] == input_y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[xlen - 1][ylen - 1]


# 最长公共子串
def longest_common_substr_dp(str1, str2):
    xlen = len(str1) + 1
    ylen = len(str2) + 1
    record = [[0 for i in range(ylen)] for j in range(xlen)]
    maxNum = 0  # 最长匹配长度
    p = 0  # 匹配的起始位

    for i in range(1, xlen):
        for j in range(1, ylen):
            if str1[i - 1] == str2[j - 1]:
                # 相同则累加
                record[i][j] = record[i - 1][j - 1] + 1
                if record[i][j] > maxNum:
                    # 获取最大匹配长度
                    maxNum = record[i][j]
                    # 记录最大匹配长度的终止位置
                    p = i
    for i in record:
        print(i)
    return str1[p - maxNum:p], maxNum


# 最长公共子序列
def longest_common_sequence(input_x, input_y):
    lcsequence_mat, flag = longest_common_sequence_dp(input_x, input_y)
    i = len(input_x)
    j = len(input_y)
    lcs = []
    get_lcs(input_x, input_y, i, j, flag, lcs)
    print((lcsequence_mat[-1][-1], lcs))


def longest_common_sequence_dp(input_x, input_y):
    xlen = len(input_x) + 1
    ylen = len(input_y) + 1
    dp = [([0] * ylen) for i in range(xlen)]
    flag = [([0] * ylen) for i in range(xlen)]
    for i in range(1, xlen):
        for j in range(1, ylen):
            if input_x[i - 1] == input_y[j - 1]:  # 不在边界上，相等就加一
                dp[i][j] = dp[i - 1][j - 1] + 1
                flag[i][j] = 0
            elif dp[i - 1][j] > dp[i][j - 1]:  # 不相等
                dp[i][j] = dp[i - 1][j]
                flag[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1]
                flag[i][j] = -1
    for dp_line in dp:
        print(dp_line)
    return dp, flag


def get_lcs(input_x, input_y, i, j, flag, lcs):
    if (i == 0 or j == 0):
        return
    if flag[i][j] == 0:
        get_lcs(input_x, input_y, i - 1, j - 1, flag, lcs)
        lcs.append(input_x[i - 1])
    elif (flag[i][j] == 1):
        get_lcs(input_x, input_y, i - 1, j, flag, lcs)
    else:
        get_lcs(input_x, input_y, i, j - 1, flag, lcs)
    return lcs


def sqrt(x):
    if x < 2:
        return x
    left, right = 0, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid < x:
            # left=mid
            left = mid + 1
            lstmid = mid  # 关键步骤
        elif mid * mid > x:
            # right=x
            right = mid - 1
        else:
            return mid
    return lstmid


"""
haspath
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], i, j):
                        return True
        return False

    def find(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i * cols + j] = '0'
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j + 1)
        elif j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j - 1)
        elif i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i + 1, j)
        elif i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i - 1, j)
        else:
            return False


"""
permutation
"""


def perm_arr(arr):
    perm = it.permutations(arr)
    return list(perm)


def perm_str(s=''):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in perm_str(s[0:i] + s[i + 1:]):
            str_list.append(s[i] + j)
    return str_list


if __name__ == '__main__':
    x = "beauty"
    y = "batyu"

    x = "abc"
    print(sqrt(5))
