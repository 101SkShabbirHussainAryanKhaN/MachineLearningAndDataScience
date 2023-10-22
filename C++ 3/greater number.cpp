#include<iostream>
using namespace std;
main()
{
	int a,b,c;
	int max;
	cout<<"enter the 1st number="<<endl;
	cin>>a;
	cout<<"enter the 2nd number="<<endl;
	cin>>b;
	cout<<"enter the 3rd number="<<endl;
	cin>>c;
	cout<<"the greater number is=";
	if(a>b)
	{
		max=a;
	}
	else
	{
		max=b;
	}
	if(b>c)
	{
		max=b;
	}
	else
	{
		max=c;
	}
	cout<<max;
}
