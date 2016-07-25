/******************************************************************
* * *
* zihadnayem8@gmail.com * *
* * *
* Dept: CSTE in NSTU,bd
* * *
* * * *
* * *
*******************************************************************/
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;
#define ll long long
ll mod(ll x,ll n,ll m)
{
   if(n==0)
   return 1;
   else if(n%2==0)
   {
      ll y=mod(x,n/2,m);
      return (y*y)%m;
   }
   else
   return ((x%m)*mod(x,n-1,m))%m;
}
 int main()
 {
  ll n,x,m;

  while(scanf("%lld %lld %lld",&x,&n,&m)!=EOF)
  {
     cout<<mod(x,n,m)<<endl;
  }

 return 0;

 }
