#include<iostream>
using namespace std;
main()
{
	int col=3;
	int row=3;
	int a[row][col],temp;
	cout<<"enter the element of row and column\n";
	for(int k=0;k<row;k++)
	{
		for(int j=0;j<col;j++)
		{
			cin>>a[k][j];
		}
	}
	for(int k=0;k<row;k++)
	{
		for(int j=0;j<col;j++)
		{
			cout<<a[k][j]<<"\t";
		}
		cout<<endl;
	}
	cout<<"The swapping of matrix:\n";
		temp=a[row][col];
		a[row][col]=a[col][row];
		a[col][row]=temp;
		
	for(int k=0;k<row;k++)
	{
		for(int j=0;j<col;j++)
		{

			cout<<a[j][k]<<"\t";
			
		}
		cout<<endl;
	}

	
}
