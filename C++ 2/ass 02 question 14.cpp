#include<iostream>
using namespace std;
main()
{
    int a1, a2, a3;
    cout<<"Enter 1st number \n";
    cin>>a1;
    cout<<"Enter 2nd number \n";
    cin>>a2;
     cout<<"Enter 3rd no number \n";
    cin>>a3;
    if(a1>a2 && a1>a3)
    {
   
       cout<<a1<<" =is greater";
    }
    else if(a2>a1 && a2>a3)
{

     cout<<a2<<" =is greater ";
}
else if(a3>a2 && a3>a1)
{

    cout<<a3<<"= is greater";

}
}

