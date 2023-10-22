#include<iostream>
using namespace std;
int function(int num1,int num2);
int main()
{
	int x,y;
	cout<<"enter two numbers:\n";
	cin>>x>>y;
	function(x,y);
	cout<<function;
}
int function(int num1,int num2)
{

	if(num1>num2)
	{
		cout<<num1<<" :is maximum and "<<num2<<" :is minimum";
	}
	else
	{ 
		cout<<num2<<" :is maximum and "<<num1<<" :is minimum";
	}	
}
