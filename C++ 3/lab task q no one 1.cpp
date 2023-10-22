#include<iostream>
using namespace std;
double addfunc(int a,int b);
double subfunc(int a,int b);
double mulfunc(int a,int b);
double divfunc(int a,int b);
double modfunc(int a,int b);
int main()
{
	int num1,num2;
	char op;
	double result;
	cout<<"enter first number:";
	cin>>num1;
	cout<<"enter second number:";
	cin>>num2;
	cout<<"enter operator:(+,-,%,*,/)";
	cin>>op;

switch(op)
{
	case'+':
		result=addfunc(num1,num2);
		cout<<"addition of"<<num1<<" and "<<num2<<" is: "<<result;
		break;
	case'-':
		result=subfunc(num1,num2);
		cout<<"subtraction of "<<num1<<" and "<<num2<<" is: "<<result;
		break;
	case'*':
		result=mulfunc(num1,num2);
		cout<<"multiplication of "<<num1<<" and "<<num2<<" is: "<<result;
		break;
	case'/':
			result=divfunc(num1,num2);
			cout<<"division of "<<num1<<" and "<<num2<<" is: "<<result;
			break;
	case'%':
		result=modfunc(num1,num2);
		cout<<"remainder of "<<num1<<" and "<<num2<<" is: "<<result;
		break;
	default:
		cout<<"invalid";
} 
}
double addfunc(int a,int b)
{
	int addition;
	addition=a+b;
	return(addition);
}
double subfunc(int a,int b)
{
	int subtraction;
	subtraction=a-b;
	return subtraction;
}
double mulfunc(int a,int b)
{
	int multiply;
	multiply=a*b;
	return multiply;
}
double divfunc(int a,int b)
{
	int divide;
	divide=a/b;
	return divide;
}
double modfunc(int a,int b)
{
	int modulo;
	modulo=a%b;
	return modulo;
}
