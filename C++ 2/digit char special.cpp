#include<iostream>
using namespace std;
main()
{
    char ch;
cout<<"Enter any charcter \t"<<endl;
cin>>ch;
if((ch >='a' && ch <='z')||(ch >='A' && ch <='Z'))
{
cout<<ch<<": is Alphabet";
}
else if(ch>='0' && ch<='9')
{
cout<<ch<<": is is a digit";
}
else
{
cout<<ch<<": is is a special character";
}
} 


    
