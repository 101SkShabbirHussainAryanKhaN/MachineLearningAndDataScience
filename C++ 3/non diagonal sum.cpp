#include<iostream>
using namespace std;
main()
{
	int arr[3][3],sum=0;
	cout<<"Enter the number:\n";
	for(int k=0;k<3;k++)
	{
		for(int j=0;j<3;j++)
		{
			cin>>arr[k][j];
		
		}
	}
	for(int k=0;k<3;k++)
	{
		for(int j=0;j<3;j++)
		{
			cout<<arr[k][j]<<"\t";
		
		}
		cout<<endl;
	}
	for(int k=0;k<3;k++)
	{
		for(int j=0;j<3;j++)
		{
				if(k!=j)
			{
				sum+=arr[k][j];
			}
		}
	}
		cout<<"sum="<<sum;
		
}
