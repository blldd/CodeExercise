# -*- coding:UTF-8 -*-

def printMatrix(matrix):
    x0 = y0 = 0
    xn = len(matrix) - 1
    yn = len(matrix[0]) - 1
    list = []
    while x0 <= xn and y0 <= yn:
        for y in range(y0, yn + 1):
            list.append(matrix[x0][y])
        for x in range(x0 + 1, xn + 1):
            list.append(matrix[x][yn])
        if x0 < xn:
            for y in range(yn - 1, y0 - 1, -1):
                list.append(matrix[xn][y])
        if y0 < yn:
            for x in range(xn - 1, x0, -1):
                list.append(matrix[x][y0])
        x0 += 1
        y0 += 1
        xn -= 1
        yn -= 1
    return list


def clockwisePrint(mat):
    ret = []
    while len(mat) > 0:
        ret += mat[0]  # 将矩阵的首行放入 ret
        # 去掉矩阵首行后逆时针旋转90度
        mat = [x for x in zip(*mat[1:])]
        mat = mat[::-1]
    return ret


# 递归
def snail_recur(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []


# 非递归
def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a


if __name__ == '__main__':
    mat = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(*mat)
    for i in zip(*mat):
        print(i)
    print(printMatrix(mat))
