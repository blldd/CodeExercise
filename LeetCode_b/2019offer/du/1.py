# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys


"""
#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXN 1005
using namespace std;

int maxw,n; 
double x,y,len;
double w[MAXN],s[MAXN];
double f[MAXN];
/*
w[i]表示前1~i辆车的重量之和 
s[i]表示第i辆车通过桥所需要的时间（单位：分钟） 
f[i]表示前i辆车通过桥的最短时间 
*/

int main()
{
    cin>>maxw>>len>>n;
    for (int i=1;i<=n;i++){
        cin>>x>>y;
        w[i]=w[i-1]+x;
        s[i]=len/y*60.00000;//注意题目中要求的是分钟，单位要转化 
    }

    for (int i=1;i<=n;i++){
        f[i]=999999999999999.0;//题目数据坑爹，初始值一定要这么大，否则会挂1~2个点 
    }

    for (int i=1;i<=n;i++){            //依次一辆一辆车枚举 
        double mint=-999999999999999.0;//mint表示车队中最慢车过桥需要的时间 
        for (int j=i;j>=1;j--){        //枚举i之前的每一辆车，相当于找到断点 
            if (w[i]-w[j-1]>maxw){     //如果车队重量大于桥的最大承受重量，跳过 
                break;
            }else{
                mint=max(mint,s[j]); 
                f[i]=min(f[i],f[j-1]+mint);// f[i-1]+mint相当于将前i辆车分为1~j-1,j~i两个车队 
            }
        }
    }

    printf("%0.1lf\n",f[n]);
}

"""



def process(N, W, w, t):
    w = [0] + w
    t = [0] + t
    res = [0 for _ in range(N + 1)]
    tmp = [[0 for i in range(N + 1)] for j in range(N + 1)]

    _sum = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        _sum[i] = _sum[i - 1] + w[i]
        tmp[i][i] = t[i]

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            tmp[i][j] = max(t[j], tmp[i][j - 1])

    for i in range(1, N + 1):
        res[i] = t[i] + res[i - 1]
        for j in range(i - 1, 0, -1):
            if _sum[i] - _sum[j - 1] <= W:
                res[i] = min(res[i], res[j - 1] + tmp[j][i])
            else:
                break
    # print(res)
    return res[N]


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    N, W = list(map(int, line.split()))

    line2 = sys.stdin.readline().strip()
    w = list(map(int, line2.split()))

    line3 = sys.stdin.readline().strip()
    t = list(map(int, line3.split()))

    # N, W, w, t = 4, 2, [1, 1, 1, 1], [2, 1, 2, 2]

    ans = process(N, W, w, t)
    print(ans)

"""
4 2
1 1 1 1
2 1 2 2
"""
