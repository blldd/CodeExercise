# # -*- coding:UTF-8 -*-
#
# import sys
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     line = list(map(int, line.split()))
#     M, N = line[0], line[1]
#
#     if M < 1 or M > 100000 or N < 1 or N > 100000:
#         print("error")
#     line = sys.stdin.readline().strip()
#     line = list(map(float, line.split()))
#
#     res = 0.0
#     if N <= M:
#         line = sorted(line)
#         m = -sys.maxsize
#         while line[-1] / 2 > line[0]:
#             tmp = line.pop() / 2
#             line.append(tmp)
#             line.append(tmp)
#             line = sorted(line)
#             m = max(m, line[-N])
#         print("%.2f" % m)
#     else:
#         line = sorted(line)
#         l = N - M
#         tmp_arr = line[-l:]
#         new_arr = line[:M]
#         for i in tmp_arr:
#             new_arr.append(i / 2)
#             new_arr.append(i / 2)
#         new_arr = sorted(new_arr)
#         print("%.2f" % new_arr[0])

# -*- coding:UTF-8 -*-
#
# import sys
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     n = int(line)
#
#     result = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         last = ""
#         cnt = 1
#         idx_arr = set()
#         arr2 = []
#         for idx, i in enumerate(line):
#             if i != last:
#                 if cnt == 2:
#                     arr2.append(idx - 1)
#                 cnt = 1
#             if i == last:
#                 cnt += 1
#
#             if cnt >= 3:
#                 idx_arr.add(idx)
#             last = i
#         if cnt == 2:
#             arr2.append(idx)
#         rmset = set()
#
#         if len(arr2) > 1:
#             last = arr2[0]
#             last_add = -1
#             for i in arr2[1:]:
#                 if i - last_add > 2 and i - last == 2:
#                     rmset.add(i)
#                     last_add = i
#                 last = i
#         res = ""
#         for idx, i in enumerate(line):
#             if idx in rmset:
#                 continue
#             if idx in idx_arr:
#                 continue
#             res += i
#         result.append(res)
#
#     for i in result:
#         print(i)
#
#

# import sys
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     cost = int(line)
#     if cost <= 0 or cost > 1024:
#         print("error")
#
#     money = 1024
#     coins = [1, 4, 16, 64]
#
#     target = money - cost
#     # print(target)
#     dp = [0 for i in range(target + 1)]
#     for i in range(1, target + 1):
#         c = sys.maxsize
#         if i - 1 >= 0:
#             c = min(c, dp[i-1] + 1)
#         if i - 4 >= 0:
#             c = min(c, dp[i-4] + 1)
#         if i - 16 >= 0:
#             c = min(c, dp[i - 16] + 1)
#         if i - 64 >= 0:
#             c = min(c, dp[i-64] + 1)
#         dp[i] = c
#     print(dp[-1])

# # -*- coding:UTF-8 -*-
#
# import sys
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     n = int(line)
#     if n < 1 or n > 100000:
#         print("error")
#
#     line = sys.stdin.readline().strip()
#     line = list(map(int, line.split()))
#
#     min_val = sys.maxsize
#     pi = 0
#     res = []
#     for idx, i in enumerate(line):
#         if idx == 0:
#             continue
#         for j in range(idx):
#             tmp = abs(i - line[j])
#             if tmp < min_val:
#                 min_val = tmp
#                 pi = j + 1
#                 ai = i
#             elif tmp == min_val:
#                 min_val = tmp
#                 if i <= ai:
#                     continue
#                 else:
#                     pi = j + 1
#
#         res.append(str(min_val) + " " + str(pi))
#
#     for i in res:
#         print(i)

# # -*- coding:UTF-8 -*-
#
# import sys
#
# if __name__ == "__main__":
#     # try:
#     #     while True:
#     line = sys.stdin.readline().strip()
#     loop = int(line)
#     if loop < 1 or loop > 10000:
#         print("error")
#     res = []
#     for lo in range(loop):
#         line = sys.stdin.readline().strip()
#         line = list(map(int, line.split()))
#         n, m = line[0], line[1]
#
#         line = sys.stdin.readline().strip()
#         line = list(map(int, line.split()))
#         x0, y0, x1, y1 = line[0] - 1, line[1] - 1, line[2], line[3]
#
#         line = sys.stdin.readline().strip()
#         line = list(map(int, line.split()))
#         x2, y2, x3, y3 = line[0] - 1, line[1] - 1, line[2], line[3]
#
#         arr = [[0 for i in range(m)] for j in range(n)]
#         w = 0
#         b = 0
#         for i in range(n):
#             for j in range(m):
#                 if i >= x2 and i < x3 and j >= y2 and j < y3:
#                     arr[i][j] = 1
#                     b += 1
#                 elif i >= x0 and i < x1 and j >= y0 and j < y1:
#                     arr[i][j] = 0
#                     w += 1
#                 elif (i + j) % 2 == 0:
#                     arr[i][j] = 0
#                     w+= 1
#                 else:
#                     arr[i][j] = 1
#                     b+=1
#
#         res.append(str(w) + " " + str(b))
#
#     for i in res:
#         print(i)

# #include<iostream>
# #include<cstdio>
# #include<queue>
# using namespace std;
# queue<int>q;
# int main()
# {
#   int n;
#   cin>>n;
#   for(int i=0;i<n;i++)
#       q.push(i+1);
#   while(!q.empty()){
#     cout<<q.front()<<" ";
#     q.pop();
#     q.push(q.front());
#     q.pop();
#   }
#   return 0;
# }

# # -*- coding:UTF-8 -*-
#
# import sys
# from queue import Queue
#
#
# if __name__ == "__main__":
#     line = sys.stdin.readline().strip()
#     n = int(line)
#     if n < 1 or n > 1000000:
#         print("error")
#     res = []
#     q = Queue()
#     for i in range(1, n+1):
#         q.put(i)
#
#     while not q.empty():
#         res.append(str(q.get()))
#         if not q.empty():
#             q.put(q.get())
#     print(" ".join(res))

# # -*- coding:UTF-8 -*-
#
# import sys
#
# if __name__ == "__main__":
#     # try:
#     #     while True:
#     ans = 0
#     line1 = sys.stdin.readline().strip()
#     n = int(line1)
#     if n < 1 or n > 10000:
#         print("error")
#     arr = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         if int(line) < 0:
#             print("error")
#             break
#         arr.append(int(line))
#
#     min_val = sys.maxsize
#
#     print(min_val)
#     # except:
#     #     pass

# # -*- coding:UTF-8 -*-
#
# import sys
#
#
# def perm(s):
#     if len(s) <= 1:
#         return [s]
#     str_list = []
#     for i in range(len(s)):
#         for j in perm(s[0:i] + s[i + 1:]):
#             str_list.append(s[i] + j)
#     return str_list
#
#
# if __name__ == "__main__":
#     # try:
#     #     while True:
#     print(perm("123"))
#     ans = 0
#     line1 = sys.stdin.readline().strip()
#
#     line1 = list(map(int, line1.split()))
#     n, a = line1[0], line1[1]
#     if n < 1 or n > 100000 or a < -1000000 or a > 1000000:
#         print("error")
#
#     line2 = sys.stdin.readline().strip()
#     line2 = list(map(int, line2.split()))
#
#     line2.append(a)
#     line2 = [str(i) for i in line2]
#     arr = perm("".join(line2))
#     min_val = sys.maxsize
#     for s in arr:
#         int_vals = [int(i) for i in s]
#         tmp = 0
#         for i in range(1, len(int_vals)):
#             tmp += abs(int_vals[i] - int_vals[i - 1])
#         min_val = min(min_val, tmp)
#
#     print(min_val)
#     # except:
#     #     pass

# import sys
# from collections import OrderedDict
#
# def is_valid(s):
#     stack1 = []
#     stack2 = []
#     for i in s:
#         if i == "(":
#             stack1.append(i)
#         elif i == ")":
#             stack1.pop()
#
# def perm(s=''):
#     if len(s) <= 1:
#         return [s]
#     str_list = []
#     for i in range(len(s)):
#         for j in perm(s[0:i] + s[i + 1:]):
#             str_list.append(s[i] + j)
#     return str_list
#
#
# if __name__ == "__main__":
#     print(perm("abd"))
#     # try:
#     #     while True:
#     ans = 0
#     line1 = sys.stdin.readline().strip()
#     line2 = sys.stdin.readline().strip()
#
#     l = len(line1) + len(line2)
#     if l % 2 == 1 or l > 2500:
#         print("error")
#
#     s = ''
#     arr = perm(line1 + line2)
#     for i in arr:
#         if is_valid(i):
#             ans += 1
#     print(ans % (pow(10, 9) + 7))
#     # except:
#     #     pass

# # -*- coding:UTF-8 -*-
#
# import sys
# from collections import OrderedDict
#
# if __name__ == "__main__":
#     # try:
#     #     while True:
#     line = sys.stdin.readline().strip()
#     line = list(map(int, line.split()))
#     n, d = line[0], line[1]
#     if n < 1 or n > 200000 or d < 1 or d > 100000000:
#         print("error")
#
#
#     od = OrderedDict()
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         line = list(map(int, line.split()))
#         od[line[0]] = line[1]
#
#     max_val = 0
#     last = [0, 0]
#     cnt = 0
#     for k, v in od.items():
#         if k - last[0] == d:
#             tmp = v + last[1]
#             max_val = max(max_val, tmp)
#             last = [k, v]
#         cnt += 1
#     print(max_val)
#     # except:
#     #     pass

# # -*- coding:UTF-8 -*-
#
# import sys
# if __name__ == "__main__":
#     # try:
#     #     while True:
#     line = sys.stdin.readline().strip()
#     line = list(map(int, line.split()))
#     n, d = line[0], line[1]
#     if n < 1 or n > 200000 or d < 1 or d > 100000000:
#         print("error")
#
#     idxs = []
#     vals = []
#     l = 0
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         line = list(map(int, line.split()))
#         idxs.append(line[0])
#         l = max(l, line[0])
#         vals.append(line[1])
#
#     arr = [0 for i in range(l)]
#     for idx, i in enumerate(idxs):
#         arr[i - 1] = vals[idx]
#
#     max_val = 0
#     for i in range(l):
#         for j in range(i+d, l):
#             tmp = arr[i] + arr[j]
#             max_val = max(max_val, tmp)
#     print(max_val)
#     # except:
#     #     pass

# # -*- coding:UTF-8 -*-
#
# import sys
# if __name__ == "__main__":
#     # try:
#     #     while True:
#     line = sys.stdin.readline().strip()
#     length = len(line)
#     if length < 1 or length > 52:
#         print("error")
#     d = {}
#     arr = []
#     s = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#          'u', 'v', 'w', 'x', 'y', 'z'}
#     for i in range(length):
#         char = line[length-i-1].lower()
#         if char not in s:
#             print("error")
#             break
#         arr.append(char)
#
#     flag = 0
#     for idx, char in enumerate(arr):
#         if char in d:
#             arr[idx] = 0
#             d[char] += 1
#             if d[char] > 2:
#                 print("error")
#                 flag = 1
#                 break
#         else:
#             d[char] = 1
#     if flag == 0:
#         for i in range(length):
#             if arr[length - 1 - i] == 0:
#                 continue
#             else:
#                 print(arr[length - 1 - i])
#                 break
#     # except:
#     #     pass

# import sys
# if __name__ == "__main__":
#     try:
#         while True:
#             n = int(sys.stdin.readline().strip())
#             ans = 0
#             if n < 1 or n > 50:
#                 print("error")
#             line = sys.stdin.readline().strip()
#             vals1 = list(map(int, line.split()))
#             if len(vals1) != n:
#                 print("error")
#             vals1 = sorted(vals1, reverse=False)
#             line = sys.stdin.readline().strip()
#             vals2 = list(map(int, line.split()))
#             vals2 = sorted(vals2, reverse=True)
#             if len(vals2) != n:
#                 print("error")
#             for idx, v in enumerate(vals1):
#                 ans += v * vals2[idx]
#             print(ans)
#     except:
#         pass


# string = "AkleBiCeilD"
# string = [i for i in string]
# for i in range(len(string))[::-1]:
#     if string[i].islower():
#         j = i
#         while string[j].islower() and j >= 1:
#             j -= 1
#         if j == 0 and string[j].islower():
#             break
#         if string[j].isupper():
#             tmp = string[j]
#             for k in range(j, i):
#                 string[k] = string[k + 1]
#             string[i] = tmp
#
# print("".join(string))
#
# # import pandas
# print("hello")
#
# #
# # print("hello world.")
# #
# # print("中文")
# #
# # # 数据类型
# # # int float str bool
# #
# # a = 3
# # b = 3.0
# # print(type(a)   # type())
# # print(type(b))
# #
# # s = "aaa"   # str
# # print(type(s))
# #
# # s2 = "123"
# # print(type(s2))
# #
# # res = str(b)  # str() 强制转换
# # print(res)
# # print(type(res))
# #
# # print(int(s2) # int() 强制转换)
# # print(type(int(2)))
# #
# # c = False
# # print(type(c))
# #
# # # 控制语句 if elif else while for
# #
# # if a < 5:
# #     print("a < 5")
# # elif a > 5:
# #     print("a > 5")
# # else:
# #     print("a = 5")
# #
# # while a < 5:
# #     print(a)
# #     a = a + 1
# #
# # print(range(0, 5))
# # print(range(1,21))
# #
# # for i in range(5):   # 遍历
# #     print(i)
# #
# # # 数据结构  list tuple set dict          tree graph linklist queue stack
# #
# # list1 = [0, 1, 2, 3, 4]    # 数组 list []  可以更改
# # print(list1)
# # print(type(list1))
# # list2 = range(5)
# # print(list2)
# # list1[0] = 5
# # print(list1)
# #
# # list3 = range(0, 10, 2)
# #
# # print(list3)
# #
# # for i in range(0,4):
# #     print(i)
# #
# # tuple1 = (0, 1, 2, 3, 4)    # 元组 tuple ()  不能更改
# # print(tuple1)
# # print(type(tuple1))
# #
# #
# # set1 = {7, 2, 5, 7, 1, 3, 2, 5, 234, 542}  # set {}  无顺序 无重复
# # print(set1)
# # print(type(set1))
# #
# #
# # dict1 = {'k1':'v2', 'k2':'v2'} # dict { : , : ,,,}  无顺序 key无重复
# # print(dict1)
# # print(type(dict1))
# #
# # print(dict1.keys())
# # print(dict1.values())
# #
# # for i in dict1.keys():
# #     print(i)
# # for i in dict1.values():
# #     print(i)
# # for i in dict1.items():
# #     print(i)
# #     print(type(i))
# #
# # set2 = set(list1)
# # print(set2)
# #
# # for i in range(10):
# #     set2.add(i)
# # print(set2)
# #
# # # for i in range(10):
# # #     set2.remove(i)
# # #     print(set2)
# #
# # print(list1)
# # list1.append(33)
# # list1.append(2)
# # print(list1)
# # list1.remove(1)
# # print(list1)
# # print(list1.count(2))
# # print(list1.index(2))
# # list1.pop()
# # print(list1)
# # list1.pop(1)
# # print(list1)
# #
# # list1.insert(0, 44)
# # print(list1)
# #
# # list1 = sorted(list1, reverse=True)
# # print(list1)
# # list1 = sorted(list1)
# # print(list1)
# #
# # rev = reversed(list1)
# # # while (rev):
# # #     print(rev.next())
# #
# # print(set2)
# # set2.pop()
# # print(set2)
# # set2.pop()
# # print(set2)
# # set2.remove(8)
# # print(set2)
# # set2.add(2)
# # set2.add(2)
# # set2.add(2)
# # print(set2)
# # print(set1)
# # print(set2.difference(set1))
# # print(set1.difference(set2))
# # print(set2.intersection(set1))
# # print(set1.union(set2))
# # print(set2)
# # set2.discard(10)
# # print(set2)
# # set2.remove(9)
# # print(("#" * 20))
# # print(set1)
# # print(set2)
# # print(set2.difference(set1))
# # set2.difference_uset2pdate(set1)
# # print
#
#
# """
# 变量
#
# 函数 （）
# 参数
#
# 数据 结构
# list   [5, 6, 7, 8, 9]   # 有重复 有顺序（默认下标0 1 2 3 。。）
# set    {5, 6, 7, 8, 9}   # 无重复 无顺序（）
# dict   {k:v, k1:v1, }
#
#
# 数据类型
# int  (integer)
# float()
# double
# str  (string)
#
#
# 控制语句   (代码中 带有 ： 都是控制语句， 他的下一行一定要空四个空格（一个tab）)
#
# if  elif  elif  else
#
# for
# while
#
#
# """
#
# a = 12        # int
# b = 3.0       # float
# c = "hello"   # ""  ''  str
# a = 3
#
# score = 67
#
# # 判断 控制语句
# if score >= 90:   # score > 90
#     print("you are great!")
# elif score > 80:  #
#     print("good")
# elif score > 70:
#     print("ok")
# elif score > 60:   # 60 < score <= 70
#     print("emmm")
# else:              #   <= 60
#     print("you are lose")
#
# # 循环控制语句
#
# print(list(range(10)))
#
# list1 = [1,3,5,7,9]
# #        0 1 2 3 4
#
# print(list1[4])
#
# for it in list1:
#     print(it)
#
# set1 = set()  # 初始化  set 无顺序的(不管这个多大，一下能找到你想找的)  无重复的  想象成一个袋子
# set1.add(3)
# set1.add(3)
# set1.add(1)
# set1.add(9)
# set1.add(-6)
# set1.add(-6)
# print(set1)
#
# print(set(list1))
#
#
#
#
#
