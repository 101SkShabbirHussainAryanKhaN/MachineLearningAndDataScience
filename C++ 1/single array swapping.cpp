#include<iostream>
using namespace std;
main()
{
	int num[]={1,2,3,4,5},temp;
	for(int k=0;k<5;k++)
	{
		cout<<num[k]<<"\t";
	}
	cout<<"\nSwap of array:\n";
	temp=num[4];
	num[4]=num[0];
	num[0]=temp;
	for(int k=0;k<5;k++)
	{
		cout<<num[k]<<"\t";
	}
}
