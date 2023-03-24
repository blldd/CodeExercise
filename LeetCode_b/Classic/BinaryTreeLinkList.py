# -*- coding:UTF-8 -*-


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    # 将二叉树转换为有序双向链表
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead == None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead


    # 获得链表的正向序和反向序
    def printList(self, head):
        while head.right:
            print(head.val)
            head = head.right
        print(head.val)
        while head:
            print(head.val)
            head = head.left

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getTreePreMid(self, pre, mid):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        root_index = mid.index(pre[0])
        root.left = self.getTreePreMid(pre[1:root_index + 1], mid[:root_index])
        root.right = self.getTreePreMid(pre[root_index + 1:], mid[root_index + 1:])
        return root


if __name__ == '__main__':
    solution = Solution()
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    middleorder_seq = [1, 2, 3, 4, 5, 6, 7]
    treeRoot = solution.getTreePreMid(preorder_seq, middleorder_seq)
    head = solution.Convert(treeRoot)
    solution.printList(head)

    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1   3 5   7
