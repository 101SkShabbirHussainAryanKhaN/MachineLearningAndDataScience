#include <iostream>
using namespace std;
int main()
{
	int i,j;
	
	int arr[3][3]={{23,24,25},{45,60,70},{90,65,78}};
	int large=arr[0][0];
	int small=arr[0][0];
	
	for(i=0;i<3;i++)
	{
	for(j=0;j<3;j++)
	if(arr[i][j]>large)
	{
			large=arr[i][j];
		
	}
	 else if(arr[i][j]>small)
	{
		small=arr[i][j];
	}

	}
	cout<<"the largest value is:"<<large<<endl;
	cout<<"the smallest value is:"<<small<<endl;		
	}
