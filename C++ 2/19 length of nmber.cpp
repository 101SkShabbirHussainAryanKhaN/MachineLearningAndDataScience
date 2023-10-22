#include <iostream>
using namespace std;
main()
{
	int n,length=0,remainder;
	cout<<"Enter any number:";
	cin>>n;
	while(n!=0)
	{
		remainder=n%10;
		length=length+1;
		n/=10;
	}
	cout<<"length of numbers="<<length;
}
