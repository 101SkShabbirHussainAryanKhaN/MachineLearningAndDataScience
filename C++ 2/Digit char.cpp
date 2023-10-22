#include<iostream>
using namespace std;
main()
{
int num;
cout<<"Enter the charcter \t"<<endl;
cin>>num;
switch(num>='a'&&num<='z')
{
case 1:
cout<<"This is Alphabat";
break;
switch(num>='A'&&num<='Z')
{
case 2:
cout<<"This is character";
break;
}
switch(num>=0 || num<=9)
{
case 3:
cout<<"this is a digit";
break;
}
default:
cout<<"This is a special character";
}
}



    
