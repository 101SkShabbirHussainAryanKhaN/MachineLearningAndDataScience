#include<iostream>
using namespace std;
main()
{
	int a1,a2,a3,a4,num;
	cout<<"enter 4 digit numbers=";
	cin>>num;
	a1=num%10;
	num=num/10;
	a2=num%10;
	num=num/10;
	a3=num%10;
	num=num/10;
	a4=num%10;
	num=num/10;
	cout<<a1<<endl<<a2<<endl<<a3<<endl<<a4;
	
}
