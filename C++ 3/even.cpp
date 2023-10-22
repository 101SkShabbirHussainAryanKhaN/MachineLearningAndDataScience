#include<iostream>
using namespace std;
main()
{
	int sum,a;
	sum=0;
	a=2;
	if(a<=100)
	{
		cout<<"the first 100 even numbers are\n";
	}
	while(a<=100)
	{
		sum=sum+a;
		a=a+2;
		a++;
	}
	cout<<sum;
}
