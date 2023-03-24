# -*- coding:UTF-8 -*-
import numpy as np


# 朴素匹配
def naive_match(s, p):
    m = len(s);
    n = len(p)
    for i in range(m - n + 1):  # 起始指针i
        if s[i:i + n] == p:
            return True
    return False


# KMP
def kmp_match(s, p):
    m = len(s);
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:
            return True
    return False


# 部分匹配表
def partial_table(p):
    '''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret


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
    return lcs


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

'''
def millerToXY(lon, lat):
    """
    :param lon: 经度
    :param lat: 维度
    :return:
    """
    L = 6381372 * math.pi * 2  # 地球周长
    W = L  # 平面展开，将周长视为X轴
    H = L / 2  # Y轴约等于周长一般
    mill = 2.3  # 米勒投影中的一个常数，范围大约在正负2.3之间
    x = lon * math.pi / 180  # 将经度从度数转换为弧度
    y = lat * math.pi / 180  # 将纬度从度数转换为弧度
    y = 1.25 * math.log(math.tan(0.25 * math.pi + 0.4 * y))  # 这里是米勒投影的转换

    # 这里将弧度转为实际距离 ，转换结果的单位是公里
    x = (W / 2) + (W / (2 * math.pi)) * x
    y = (H / 2) - (H / (2 * mill)) * y
    return (x, y)

def extract_common_sequence(lcs_mat, is_equal):
    # 获得seqA与seqB的长度
    n, m = is_equal.shape
    # 公共序列在序列A中的索引
    subSeqAIndex = []
    # 公共序列在序列B中的索引
    subSeqBIndex = []
    i = n - 1
    j = m - 1
    # 回溯寻找
    while i != 0 and j != 0:
        if is_equal[i][j] == 1:
            # 如果这两个值都相等，那么回溯到isEqual[i-1][i-1]
            subSeqAIndex.insert(0, i)
            subSeqBIndex.insert(0, j)
            i = i - 1
            j = j - 1
        elif lcs_mat[i + 1][j] >= lcs_mat[i][j + 1]:
            # 进入到这里，说明不相等，且矩阵矩阵左边大于上面
            # 即lcsMat[i+1][j+1]是由lcsMat[i+1][j]得到，向左回退，因此j回退
            j = j - 1
        else:
            # 进入到这里，说明不相等，且矩阵上面大于左边
            # 即lcsMat[i+1][j+1]是由lcsMat[i][j+1]得到，向上回退，因此j回退
            i = i - 1
    return [subSeqAIndex, subSeqBIndex]


def longest_common_subsequence(seq_a, seq_b, tol):
    """
    循环求解最长公共子序列
    """
    # 获取序列A的长度
    n = len(seq_a)
    # 获取序列B的长度
    m = len(seq_b)
    # 生成0矩阵，序列矩阵lcsMat[i][j]
    # lcs_mat[i][j]：表示seqA前i个序列与seqB前j个序列的最长公共子序列长度
    # lcs_mat[0][j]，与lcsMat[i][0]都为0，即，当一个序列为0时，没有公共子序列
    lcs_mat = np.zeros((n + 1, m + 1), dtype=np.int)
    # 计算任意两个点的距离
    disMat = cdist(seq_a, seq_b, metric='euclidean')
    # 用于判断，元素是否相等
    # is_equal[i][j]==1表示seqA[i]==seq_b[j]
    # is_equal[i][j]==0表示seqA[i]!=seq_b[j]
    is_equal = np.where(disMat < tol, 1, 0)
    # 循环为lcsMat赋值
    # lcs_mat[n][m]为最长公共子序列的长度
    for i in range(n):
        # 为lcsMat一行一行的赋值（注意：要思考为什么可以一行一行的赋值）
        # 原因：lcs_mat[i][j]的值仅与三个位置有关，分别为：lcs_mat[i-1][j-1]、lcs_mat[i-1][j]、lcs_mat[i][j-1]
        # 因此每一次迭代，所有的三个元素肯定都已经有值了
        for j in range(m):
            # seq_a[i]seq_b[j]的公共子序列长度，记录在lcsMat[i + 1][j + 1]
            # 因为有了0序列，矩阵多了一行一列（均为0）
            if is_equal[i][j] == 1:
                # 如果最后一个元素相等，那么就是lcsMat[i][j]+1，即当前元素等于左上角元素加1
                lcs_mat[i + 1][j + 1] = lcs_mat[i][j] + 1
            else:
                # 如果最后一个元素不相等，即当前元素等于左边元素或者上面元素中最大的那个
                lcs_mat[i + 1][j + 1] = max(lcs_mat[i + 1][j], lcs_mat[i][j + 1])
    # 用于求解公共子序列相应的位置
    sequence = extract_common_sequence(lcs_mat, is_equal)
    # 用于计算相似度
    similarity = lcs_mat[n][m] * 1.0 / min(n, m)
    return lcs_mat[n][m], similarity, sequence
'''


if __name__ == '__main__':
    # print(naive_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
    # print(partial_table("ABCDABD"))
    # print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))

    x = "beauty"
    y = "batyu"

    print(longest_common_sequence(x, y))
    # print(longest_common_substr_dp(x, y))
