#include<iostream>
using namespace std;
main()
{
	int m[4][4],sum=0;
	cout<<"Enter the number:\n";
	for(int k=0;k<4;k++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>m[k][j];
		
		}
	}
	for(int k=0;k<4;k++)
	{
		for(int j=0;j<4;j++)
		{
			cout<<m[k][j]<<"\t";
		
		}
		cout<<endl;
	}
	for(int k=0;k<4;k++)
	{
		for(int j=0;j<4;j++)
		{
				if(k==j)
			{
				sum+=m[k][j];
			}
		}
	}
		cout<<"sum of diagonal= "<<sum;
		
}
