#include<iostream>
using namespace std;
main()
{
	int num,div;
	div=num/5;
	div=num/11;
	cout<<"Enter the number="<<endl;
	cin>>num;
	switch(div)
	{
		case'num/5':
		cout<<"the number is divisible by 5"<<endl;
		break;
		case'num/11':
			cout<<"the number is divisible by 11"<<endl;
			break;
		default:
		cout<<"the number is not divisible by 5 nor 11";
	}
}
