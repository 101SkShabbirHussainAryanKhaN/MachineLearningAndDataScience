#include<iostream>
using namespace std;
int result(int num);
main()
{
	int x;
	cout<<"enter any number:";
	cin>>x;
	cout<<result(x);
}
int result(int num)
{
	if(num%2==0)
	{
		cout<<num<<" is even number\n";
	}
	else
	{
		cout<<num<<" is an odd number\n";
	}
	return 0;
}
