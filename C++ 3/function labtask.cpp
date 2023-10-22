#include<iostream>
using namespace std;
double raistopower(int base, int power);//function decleration
int main()
{
	int basefrommain, powerfrommain;
	double result;
	cout<<"enter any base value";
	cin>>basefrommain;
	cout<<"enter degree of value";
	cin>>powerfrommain;
	result=raistopower(basefrommain,powerfrommain);
	cout<<basefrommain<<"^"<<powerfrommain<<"is"<<result;
}

double raistopower(int base , int power)
{
	int result;
	for (int i=1;i<power;i++)
	{
	double result=1;
	result*=base ;
	}
	return (result);
}
