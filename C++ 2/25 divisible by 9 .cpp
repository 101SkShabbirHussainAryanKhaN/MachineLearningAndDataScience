#include<iostream>
using namespace std;
int main()
{
	int i,sum=0;
	for(i=100;i<=200;i++)
	{
		if(i%9==0)
		{
			sum+=i;
		cout<<i<<"+";
		}
	
	}
	
	cout<<sum;
	cout<<"\nSum of integer between 100 ans 200 which are divisible by 9 is = "<<sum;
return 0;
}

