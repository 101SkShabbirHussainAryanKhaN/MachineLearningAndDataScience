#include<iostream>
using namespace std;
int main()
{
	int num;
	cout<<"Enter a number\n";
	cin>>num;
	if(num%2==0)
	{
		cout<<num<<"=is Even";
	}
	else if(num%2!=0)
	{
	cout<<num<<"=is Odd";	
	}
	else
	cout<<"invalid entry";
return 0;
}

