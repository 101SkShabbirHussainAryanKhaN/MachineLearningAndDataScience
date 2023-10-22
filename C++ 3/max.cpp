#include<iostream>
using namespace std;
main()
{
	float x, y,z, max;
	cout<<"enter the firts value :";
	cin>>x;
	cout<<"enter the second value :";
	cin>>y;
	cout<<"enter the third value :";
	cin>>z;
	if(x>y)
	{
		if(x>z)
		{
			max=x;
		}			
			else
			{
				max=z;	
			}			
	}		
	else
	{
		if(y>z)
		{
			max=y;
		}		
			else
			{
				max=z;	
			}
				
	}
			
		cout<<"Max value is:"<<max;
 } 


