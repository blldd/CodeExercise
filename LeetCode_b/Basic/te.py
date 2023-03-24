import pysnooper
import torch

# @pysnooper.snoop()
# def number_to_bits(number):
#     if number:
#         bits = []
#         while number:
#             number, remainder = divmod(number, 2)
#             bits.insert(0, remainder)
#         return bits
#     else:
#         return [0]
#
# number_to_bits(6)

A = [[1, 2, 0, 0], [0, 4, 0, 0], [4, 0, 0, 1], [1, 0, 1, 0]]
A = torch.FloatTensor(A)
print(torch.eye(4))
A = A + torch.eye(4)
# 所有节点的度
d = A.sum(1)
print(d)