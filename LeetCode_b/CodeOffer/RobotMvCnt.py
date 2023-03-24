# -*- coding:UTF-8 -*-

'''
分析：回溯算法

'''


class Solution(object):
    def mvCnt(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows < 0 or cols < 0:
            return 0
        visited = [[0 for j in range(cols)] for i in range(rows)]
        # print(visited)
        cnt = self.mvCntCore(threshold, rows, cols, 0, 0, visited)
        return cnt

    def mvCntCore(self, threshold, rows, cols, row, col, visited):
        cnt = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row][col] = 1
            cnt = 1 + self.mvCntCore(threshold, rows, cols, row - 1, col, visited) + \
                  self.mvCntCore(threshold, rows, cols, row, col - 1, visited) + \
                  self.mvCntCore(threshold, rows, cols, row + 1, col, visited) + \
                  self.mvCntCore(threshold, rows, cols, row, col + 1, visited)
        return cnt

    def check(self, threshold, rows, cols, row, col, visited):
        if row in range(rows) and col in range(cols) \
                and self.getDigitSum(row) + self.getDigitSum(col) <= threshold \
                and not visited[row][col]:
            return True
        return False

    def getDigitSum(self, num):
        sum = 0
        for d in str(num):
            sum += int(d)
        return sum


if __name__ == '__main__':
    threshold = 9
    rows = 6
    cols = 6

    print(Solution().mvCnt(threshold, rows, cols))
