#include<iostream>
using namespace std;
int main()
{
int arr[2][2]={{12,24},{24,12}};
int sum=0;
	for(int k=0;k<2;k++)
	{
		for(int j=0;j<2;j++)
		{
			cout<<arr[k][j]<<"\t";
		
		}
		cout<<endl;
	}
	for(int k=0;k<2;k++)
	{
		for(int j=0;j<2;j++)
		{
				if(k!=j)
			{
				sum=sum+arr[k][j];
			}
		}
	}
		cout<<"sum of diagonal= "<<sum;
		
}
