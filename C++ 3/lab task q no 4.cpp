#include<iostream>
using namespace std;
int func(int n);
main()
{
	int n;
	cout<<"enter the number:";
	cin>>n;
	func(n);	
}
int func(int n)
{
	for (int i=0;i<=n;i++)
	{
		if (i%2==0)
		{
			cout<<i<<" ";
		}
	}	
}
