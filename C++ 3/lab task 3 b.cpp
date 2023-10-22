#include<iostream>
using namespace std;
main()
{
	int num1, num2, num3,num=4567, next, next1, next2;
	next=num/10;
	num1=num%10;
	next1=next/10;
	num2=next%10;
	next2=next1/10;
	num3=next1%10;
	cout<<next2<<"                                                                                                                       ";
	cout<<num3<<"                                                                                                                       ";
	cout<<num2<<"                                                                                                                       ";
	cout<<num1<<endl;
	
}
