//write a program to find sum,mul,sub of two numbers
#include<iostream>
using namespace std;
main()
{
	int a,b,c;
	cout<<"Enter Any two numbers :";
	cin>>a>>b;
	c=a+b;
	c++;
	cout<<"addition of two numbers is:"<<c<<endl;
	c=a-b;
	cout<<"Subtraction of two numbers is:"<<c<<endl;
	c=a*b;
	cout<<"Multiplication of two numbers is:"<<c<<endl;
	c=a/b;
	cout<<"Division of two numbers is:"<<c<<endl;
	c=a%b;
	cout<<"MOdulus of two numbers is:"<<c<<endl;

}
