#include<iostream>
using namespace std;
int main()
{
	char ch;
cout<<"Enter any Aphabat\t"<<endl;
cin>>ch;
switch(ch>='a' && ch<='z')
{
case 1:
cout<<"it is lower case alphabat";
break;
}
switch(ch>='A' && ch<='Z')
{
case 2:
cout<<"it is upper case alphabat";
break;
defualt:
cout<<"invalid character";
}
return 0;
} 


    