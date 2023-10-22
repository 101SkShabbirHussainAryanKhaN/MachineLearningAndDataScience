#include<iostream>
using namespace std;
int main(){
	int r,c,i,j;
	int highest,lowest;
	int array[5][5];
	cout<<"Enter the no of rows : "<<endl;
	cin>>r;
	cout<<"Enter the no of column : "<<endl;
	cin>>c;
	cout<<endl<<"Enter the matrix : "<<endl;
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		cin>>array[i][j];
	}
	highest=array[0][0];
	lowest=array[0][0];
	for(i=0;i<r;++i){
		for(j=0;j<c;++j)
		{
			if(array[i][j]>highest)
			highest=array[i][j];
			else
			if(array[i][j]<lowest)
			lowest=array[i][j];
		}
		}
		cout<<endl<<"Highest element is : "<<highest<<endl;
		cout<<endl<<"Lowest element is : "<<lowest<<endl;
return 0;		
		
	}
	
	

