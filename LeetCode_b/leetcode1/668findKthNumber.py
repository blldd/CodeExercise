# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/15 8:18 AM
@Author  : ddlee
@File    : 668findKthNumber.py
"""

"""
给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。

例 1：
输入: m = 3, n = 3, k = 5
输出: 3
解释: 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def cnt_before_x(x):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(x // i, n)
            return cnt

        def binary_search(left, right, k):
            while left < right:
                mid = (left + right) >> 1
                cnt = cnt_before_x(mid)
                if cnt >= k:
                    right = mid
                else:
                    left = mid + 1
            return left

        left = 1
        right = m * n + 1
        kth = binary_search(left, right, k)
        return kth


    """
    class Solution {
    public:
        int help(int m,int n,int mid,int k){
            
            int k1=0,k2=0;
            for(int i=1;i<=m;i++){
                k1+=min((mid-1)/i,n);
                k2+=min(mid/i,n);
            }
            
            if(k1<k&&k<=k2)return 0;
            else if(k1>=k)return 1;
            else return -1;
        }
        int findKthNumber(int m, int n, int k) {
            int s=m+n;m=max(m,n);n=s-m;//保证m>=n
            int fir=0,end=m*n+1;
            while(fir<end){
                int mid=(fir+end)/2;
                int h=help(m,n,mid,k);
                if(h==0)return mid;
                else if(h==1)end=mid;
                else fir=mid;
            }
            return 0;
        }
    };
    """

    def findKthNumber2(self, m: int, n: int, k: int) -> int:
        """
        有bug
        :param m:
        :param n:
        :param k:
        :return:
        """
        def cnt_before_x(x):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(x // i, n)
            return cnt

        def binary_search(left, right, k):
            while left < right:
                mid = (left + right) >> 1
                cnt = cnt_before_x(mid)
                if cnt >= k:
                    right = mid
                else:
                    left = mid + 1
            return left

        left = 1
        right = m * n + 1
        kth = binary_search(left, right, k)
        return kth


if __name__ == '__main__':
    m = 11
    n = 11
    k = 77
    print(Solution().findKthNumber2(m, n, k))
    print("**" * 10)
    print(Solution().findKthNumber(m, n, k))
