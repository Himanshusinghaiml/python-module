/* maximum product subarray
inpt=[-1,-3,-10,0,60]  */
#include<bits/stdc++.h>
using namespace std;

int main()
{
  unordered_map<int,int>m;
  int arr[]={2,3,6,3,4,1,3,6};
  int n=8;  
  for(int i=0;i<n;i++)
  {
    m[arr[i]]++;
  }
 for(auto  i:m)
 {
     if(i.second>1)
     {
        cout<<i.first<<" ";
     }
 }
}
