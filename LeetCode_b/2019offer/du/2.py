# -*- coding: utf-8 -*-
"""
@Time    : 2019/7/28 3:01 PM
@Author  : ddlee
@File    : 1.py
"""

import sys
import math


def process(n, arr):

    pass


if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     line = sys.stdin.readline().strip()
#     arr = list(map(int, line.split()))

    n, arr = 5, [1, 2, 3, 4, 5]

    res = process(n, arr)
    print(res)

"""
5
1 2 3 4 5
"""



"""

#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
int n,kk,y,z,x;;
long long f[2010][2010],sz[2010];
vector<pair<int,int> > a[2010];
void dfs(int x,int fa)
{
    f[x][0]=f[x][1]=0; 
    int u;
    long long ans; 
    sz[x]=1;
    for (int i=0;i<a[x].size();i++)
      {
          u=a[x][i].first;
         if (u==fa) continue;
         dfs(u,x);
         sz[x]+=sz[u];
       for(int j=sz[x];j>=0;j--)
        {
          for(int k=0;k<=sz[u]&&k<=j;k++)
          {
            ans=(long long)(k*(kk-k))+(long long)((sz[u]-k)*(n-kk-(sz[u]-k))); 
            ans*=a[x][i].second;
            ans+=f[u][k];
            f[x][j]=max(f[x][j],f[x][j-k]+ans);
          }
        }

      }
}
int main()
{
    freopen("haoi2015_t1.in","r",stdin);
    freopen("haoi2015_t1.out","w",stdout); 
    scanf("%d%d",&n,&kk);
    for (int i=1;i<=n-1;i++)
      {
         scanf("%d%d%d",&x,&y,&z);
         a[x].push_back(make_pair(y,z));
         a[y].push_back(make_pair(x,z));
      }
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
         f[i][j]=-999999999999;
    dfs(1,0);
    printf("%lld",f[1][kk]); 
}

"""