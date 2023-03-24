# -*- coding:UTF-8 -*-

"""
给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？
树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向父节点的指针。

根据中序遍历的特点：

若该节点有右子树:
    则下一个节点为右子树最左边的节点
若该节点无右子树：
    若该节点是父节点的左节点，则下一个节点为父节点
    若该节点是父节点的右节点，则下一个节点为遍历父节点找到一个节点是其父节点左孩子的节点
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def __init__(self, BinaryTree, Node):
        self.BinaryTree = BinaryTree
        self.Node = Node

    def findNextInOrder(self):
        if self.BinaryTree is None:
            return None
        # 存在右子树
        if self.Node.right is not None:
            nextNode = self.Node.right
            while nextNode.left != None:
                nextNode = nextNode.left
            return nextNode
        else:
            # 如果是父节点的左节点
            if self.Node.parent.left == self.Node:
                return self.Node.parent
            # 如果是父节点的右节点
            else:
                nextNode = self.Node.parent
                while nextNode != None:
                    if nextNode.parent.left == nextNode:
                        return nextNode.parent
                    nextNode = nextNode.parent
                return None

    def findNextPreOrder(self):
        if self.BinaryTree is None:
            return None
        # 存在左子树
        if self.Node.left is not None:
            nextNode = self.Node.left
            return nextNode
        else:
            # 若该节点是父节点的左节点
            if self.Node.parent.left == self.Node:
                nextNode = self.Node.parent
                while nextNode != None:
                    if nextNode.right:
                        return nextNode.right
                    nextNode = nextNode.parent
                return None
            else:
                nextNode = self.Node.parent
                if nextNode.parent:
                    nextNode = nextNode.parent
                else:
                    return None
                while nextNode != None:
                    if nextNode.right:
                        return nextNode.right
                    nextNode = nextNode.parent
                return None


if __name__ == '__main__':
    """
             0
           /   \
          1     3
         / \
        4   5
       / 
      6
     / \
    8   7
    """
    root = TreeNode(0)
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)
    f = TreeNode(7)
    g = TreeNode(8)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    c.left = e
    e.right = f
    e.left = g
    a.parent = root
    b.parent = root
    c.parent = a
    d.parent = a
    e.parent = c
    g.parent = e
    f.parent = e

    print(Solution(root, d).findNextPreOrder())
