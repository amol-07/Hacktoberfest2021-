#include <bits/stdc++.h>
using namespace std;
// #define ll long long int

ll mult(int i)
{
    vector<int> ans;
    ll tp;
    while(i>0)
    {
        tp = i%10;
        i = (int)i/10;
        ans.push_back(tp);
    }
    ll mul = 1;
    for (ll j=0; j<ans.size();j++)
    {
        mul*=ans[j];
    }
    return mul;
}

void fun()
{
        ll t;
    // cin>>t;
    
    t = 1;
    while(t--)
    {
        ll x = 1000000-1;
       // cin>>x;
        string y = to_string(x);


        if (x==0)
            cout<<1;
        else if (x<10)
            cout<<(x);
        else
        {
            int fct;
            int fact[] = {1,2,6,24,120,720, 5040};
            ll count = 0;
            for(int i = 1; i<=x; i++)
            {
                int flag=0;
                string dd = to_string(i);
                for (auto &ch: dd)
                    if (&ch == "0")
                    {
                        flag=1;
                        break;
                    }
                if (flag == 0)
                {
                    ll mul = mult(i);
                    fct = fact[dd.length() -1];
                    if (mul>=fct)
                        count++;
                }
            }
            cout<<(count);
        }
    }
    
}
