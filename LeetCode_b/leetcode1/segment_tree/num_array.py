# -*- coding: utf-8 -*-
"""
@Time    : 2019/10/4 3:28 PM
@Author  : ddlee
@File    : num_array.py
"""
"""
307. 区域和检索 - 数组可修改

给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。

示例:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
说明:

数组仅可以在 update 函数下进行修改。
"""


class SegmentTree:
    def __init__(self, data, merge):
        '''
        data:传入的数组
        merge:处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        '''

        self.data = data
        self.n = len(data)
        #  申请4倍data长度的空间来存线段树节点
        self.tree = [None] * (4 * self.n)  # 索引i的左孩子索引为2i+1，右孩子为2i+2
        self._merge = merge
        if self.n:
            self._build(0, 0, self.n - 1)

    def query(self, ql, qr):
        '''
        返回区间[ql,..,qr]的值
        '''
        return self._query(0, 0, self.n - 1, ql, qr)

    def update(self, index, value):
        # 将data数组index位置的值更新为value,然后递归更新线段树中被影响的各节点的值
        self.data[index] = value
        self._update(0, 0, self.n - 1, index)

    def _build(self, tree_index, l, r):
        '''
        递归创建线段树
        tree_index : 线段树节点在数组中位置
        l, r : 该节点表示的区间的左,右边界
        '''
        if l == r:
            self.tree[tree_index] = self.data[l]
            return

        mid = (l + r) >> 1  # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = 2 * tree_index + 1, 2 * tree_index + 2  # tree_index的左右子树索引
        self._build(left, l, mid)
        self._build(right, mid + 1, r)

        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

    def _query(self, tree_index, l, r, ql, qr):
        '''
        递归查询区间[ql,..,qr]的值
        tree_index : 某个根节点的索引
        l, r : 该节点表示的区间的左右边界
        ql, qr: 待查询区间的左右边界
        '''
        if l == ql and r == qr:
            return self.tree[tree_index]

        mid = (l + r) // 2  # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            # 查询区间全在左子树
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            # 查询区间全在右子树
            return self._query(right, mid + 1, r, ql, qr)

        # 查询区间一部分在左子树一部分在右子树
        return self._merge(self._query(left, l, mid, ql, mid),
                           self._query(right, mid + 1, r, mid + 1, qr))

    def _update(self, tree_index, l, r, index):
        '''
        tree_index:某个根节点索引
        l, r : 此根节点代表区间的左右边界
        index : 更新的值的索引
        '''
        if l == r == index:
            self.tree[tree_index] = self.data[index]
            return

        mid = (l + r) // 2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2

        if index > mid:
            # 要更新的区间在右子树
            self._update(right, mid + 1, r, index)
        else:
            # 要更新的区间在左子树index<=mid
            self._update(left, l, mid, index)

        # 里面的小区间变化了，包裹的大区间也要更新
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])


class NumArray:

    def __init__(self, nums):
        self.segment_tree = SegmentTree(nums, lambda x, y: x + y)

    def update(self, i: int, val: int) -> None:
        self.segment_tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.segment_tree.query(i, j)


if __name__ == '__main__':
    nums = [1, 3, 5]
    obj = NumArray(nums)
    obj.update(1, 2)
    param_2 = obj.sumRange(0, 2)
    print(param_2)
