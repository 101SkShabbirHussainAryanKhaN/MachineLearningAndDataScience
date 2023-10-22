#include<iostream>
using namespace std;
main()
{
	int num,even=0;
	cout<<"the sum of 100 even numbers:";
	for(int i=0;i<=100;i++)
	{
		if(num%2==0)
		{
			even=even+i;
			
		}
		cout<<"the even numbers"<<num+i<<"\b="<<even;
	}
}
