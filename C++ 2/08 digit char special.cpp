#include<iostream>
using namespace std;
int main()
{
     char ch;
cout<<"Enter any charcter \t"<<endl;
cin>>ch;
if((ch >= 'a' && ch <= 'z')||(ch >= 'A' && ch <= 'Z'))
{
cout<<ch<<": is Alphabat";
}
else if(ch>= '0' && ch<= '9')
{
cout<<ch<<": is is a digit";
}
else
{
cout<<ch<<": is is a special character";
}
return 0;
} 


    