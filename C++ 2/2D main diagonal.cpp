#include <iostream>
using namespace std;
int main()
{
	int i,j,sum=0;
	
	int arr[3][3]={{23,24,25},{45,60,70},{90,65,78}};
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		cout<<arr[i][j]<<"\t";
		cout<<endl;
	}
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
	if(i==j)
	{
			
		sum=sum+arr[i][j];
		}
		
	}
		
	
	
	cout<<"\nSum of diagonal elements is:"<<sum;
	
	
return 0;
}

