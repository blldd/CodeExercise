# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


# from sklearn import metrics
#
#
# def auc_fun(true, pred):
#     fpr, tpr, thresholds = metrics.roc_curve(true, pred, pos_label=1)
#     # print(fpr)
#     # print(tpr)
#     return metrics.auc(fpr, tpr)

def read_data(arr):
    db = []  # (score,nonclk,clk)
    pos, neg = 0, 0  # 正负样本数量
    # 读取数据
    for line in arr:
        score = float(line[1])
        trueLabel = int(line[0])

        if trueLabel == 1.0:
            sample = [score, 0, 1]
        else:
            sample = [score, 1, 0]
        score, nonclk, clk = sample
        pos += clk  # 正样本
        neg += nonclk  # 负样本
        db.append(sample)

    return db, pos, neg


def get_roc(db, pos, neg):
    # 按照输出概率，从大到小排序
    db = sorted(db, key=lambda x: x[0], reverse=True)

    # 计算ROC坐标点
    xy_arr = []
    tp, fp = 0., 0.
    for i in range(len(db)):
        tp += db[i][2]
        fp += db[i][1]
        xy_arr.append([fp / neg, tp / pos])
    return xy_arr


def get_AUC(xy_arr):
    # 计算曲线下面积
    auc = 0.
    prev_x = 0
    for x, y in xy_arr:
        if x != prev_x:
            auc += (x - prev_x) * y
            prev_x = x
    return auc


def process(arr, N):
    db, pos, neg = read_data(arr)
    xy_arr = get_roc(db, pos, neg)
    auc = get_AUC(xy_arr)
    return auc


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    N = int(line1)

    arr = []
    for i in range(N):
        line2 = sys.stdin.readline().strip()
        values2 = list(map(float, line2.split()))
        arr.append(values2)

    ans = process(arr, N)
    print("%.2f" % ans)

"""
10
1 0.90
0 0.70
1 0.60
1 0.55
0 0.52
1 0.40
0 0.38
0 0.35
1 0.31
0 0.10
"""
