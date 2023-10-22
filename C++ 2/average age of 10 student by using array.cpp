#include <iostream>
using namespace std;
int main()
{
	float age[10],avgAge=0;
	for(int i=0;i<=9;i++)
	{
		cout<<"Enter an age:";
		cin>>age[i];
		
	}
	for(int i=0;i<=9;i++)
	{
		avgAge=avgAge+age[i];
	}
	cout <<"average Age is:"<<avgAge/10;
return 0;
}

