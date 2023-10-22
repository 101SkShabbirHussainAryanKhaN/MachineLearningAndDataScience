#include <iostream>
using namespace std;
int max(int ,int);
int main()
{
int num1,num2;
cout<<"enter first number=\n";
cin>>num1;
cout<<"enter second number=\n";
cin>>num2;
max(num1,num2);
}
int max(int a, int b)
{
	if(a>b)
	{
		cout<<a<<":num1 is maximum";
	}
	else
	{
		cout<<b<<": num2 is maximum";
	}
	return a,b;
	
}

