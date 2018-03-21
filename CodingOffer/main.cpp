#include <stdio.h>
#include <string.h>
#include <iostream>
#include <cmath>
using namespace std;
long long  a[10000];

int gcd(int x,int y)
{
    while(x!=y)
    {
        if(x>y)
            x=x-y;
        else
            y=y-x;
    }
    return x;
}


int main()
{

    a[1]=0;
    a[2]=3;
    for(int i=3; i<5000; i++)
    {
        int num=0;
        for(int j=2; j<i; j++)
        {
            if(gcd(i,j)==1);
            num++;
        }
        a[i]=a[i-1]+num*2;
        // cout<<i<<"-"<<a[i]<<endl;
    }

    int n;
    while(cin>>n)
    {
        cout<<a[n+1]<<endl;
    }
}
