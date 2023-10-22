#include<iostream>
using namespace std;
main()
{
	int a[3][3], b[3][3];
	cout<<"enter value of first matrix"<<endl;
	for(int row=0; row<3;row++){
		for(int col=0; col<3; col++)
		{
			cin>>a[row][col];
		}
	}
	cout<<"enter value of second matrix"<<endl;
	for(int row=0; row<3;row++){
		for(int col=0; col<3; col++)
		{
			cin>>b[row][col];
		}
	}
	cout<<"addition of two matrices"<<endl;
	for(int row=0; row<3;row++){
		for(int col=0; col<3; col++)
		{
			cout<<a[row][col]+b[row][col]<<"\t";
		}
		cout<<endl;
	}
}
