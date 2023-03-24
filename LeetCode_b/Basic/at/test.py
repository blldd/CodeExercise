# -*- coding:UTF-8 -*-
import math
import sys


# Read only region start
class UserMainCode(object):
    @classmethod
    def honey(cls, input1, input2, input3, input4, input5, input6):
        '''
        input1 : int
        input2 : int
        input3 : int[-]
        input4 : int[-]
        input5 : int[]
        input6 : int

        Expected return type : int
        '''
        # Read only region end
        # Write code here
        flower = input3
        honeys = input4
        source = input5
        period = input6

        dis = math.sqrt(pow(source[0] - flower[0][0], 2) + pow(source[1] - flower[0][1], 2))
        while dis < period:
            dis

if __name__ == '__main__':
    print(UserMainCode().honey(5, 3, [[1, 0], [3, 3], [2, 2]]))

#

#
# # Read only region start
# class UserMainCode(object):
#     @classmethod
#     def findPosition(cls, input1, input2, input3):
#         '''
#         input1 : int
#         input2 : int
#         input3 : int[-]
#
#         Expected return type : int
#         '''
#         # Read only region end
#         # Write code here
#
#         res = 0
#         arr = list(range(input1))
#         for x, y in input3:
#             if x == 1:
#                 arr.pop(0)
#             if x == 3:
#                 res += arr.index(y - 1) + 1
#             if x == 2:
#                 idx = arr.index(y - 1)
#                 arr.pop(idx)
#         return res



# # -*- coding:UTF-8 -*-
#
# import sys
#
#
# def shrink(s):
#     length = len(s)
#     if length % 2 == 1:
#         return s
#     if length % 2 == 0 and s[:(length // 2)] == s[(length // 2):]:
#         return shrink(s[:(length // 2)])
#     else:
#         return s
#
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     length = len(line)
#
#     if length > 1000000:
#         print("error")
#
#     line = shrink(line)
#     # print(line)
#     cnt = 0
#     _set = set()
#     for i in range(length):
#         tmp = line[i:] + line[:i]
#         if tmp not in _set:
#             cnt += 1
#             _set.add(tmp)
#
#     print(cnt)

# import math
#
#
# def sieve(size):
#     sieve = [True] * size
#
#     sieve[0] = False
#
#     sieve[1] = False
#
#     for i in range(2, int(math.sqrt(size)) + 1):
#
#         k = i * 2
#
#         while k < size:
#             sieve[k] = False
#
#             k += i
#
#     return sum(1 for x in sieve if x)
#
#
# print(sieve(10000000000))
