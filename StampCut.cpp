#include <iostream>  
#include <cstring>  
#include <algorithm>  
#include <queue>  
using namespace std;  
int a[12]= {1,2,3,4,6,7,8,9,11,12,13,14},vis[20];  
int main()  
{  
    int sum=0;  
    for(int i1=0; i1<12; i1++)  
        for(int i2=i1+1; i2<12; i2++)  
            for(int i3=i2+1; i3<12; i3++)  
                for(int i4=i3+1; i4<12; i4++)  
                    for(int i5=i4+1; i5<12; i5++)  
                    {  
                        memset (vis,0,sizeof(vis));  
                        int p=0;  
                        vis[a[i1]]=1;
                        vis[a[i2]]=1;  
                        vis[a[i3]]=1;  
                        vis[a[i4]]=1;  
                        vis[a[i5]]=1;  
                        queue<int>q;  
                        q.push(a[i1]);  
                        vis[a[i1]]=0;  
                        while(!q.empty())  
                        {  
                            int top=q.front();  
                            q.pop();  
                            p++;  
                            if(vis[top+1]) { q.push(top+1);vis[top+1]=0; }  //right
                            if(vis[top+5]) { q.push(top+5);vis[top+5]=0; }  //down
                            if(vis[top-1]) { q.push(top-1);vis[top-1]=0; }  //left
                            if(vis[top-5]) { q.push(top-5);vis[top-5]=0; }  //up
                        }  
                        if(p==5)  //if there is five elments linked
                        {  
                            sum++;  
                            cout<<a[i1]<<" "<<a[i2]<<" "<<a[i3]<<" "<<a[i4]<<" "<<a[i5]<<endl;  
                        }  
                    }  
    cout<<sum<<endl;  
  
    return 0;  
}  