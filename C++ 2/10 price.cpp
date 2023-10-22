#include <iostream>
using namespace std;
int main()
{
	int values[4],even=0,sum=0,prime=0;
	for(int i=0;i<=3;i++)
	{
	if(values[i%2==0])
	{
		even=even+values[i];
		
	}
		cout<<"Enter Price:";
		cin>>values[i];
		sum=sum+values[i];
		
	}
	cout<<even<<","<<endl;
	cout<<"the sum of input number is:"<<sum;

	
return 0;
}

