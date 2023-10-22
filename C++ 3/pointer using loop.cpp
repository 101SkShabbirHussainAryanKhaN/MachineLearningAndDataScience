#include <iostream>
using namespace std;
int main()
{
	while(true)
	{
	int const maxSize=4;
	int myArray[maxSize];
	int *ptr=myArray;
	cout<<"\t\t\t---------------------------------------------\n";
	cout<<"\t\t\t*****************    ********  *************\n";
	cout<<"\t\t\tEnter element of an array:\n\t\t\t";
	
	for(int i=0;i<4;i++)
	{
		cin>>*(ptr+i);
	}
	cout<<"\t\t\tArray elements:\n\t\t\t";
	for(int i=0;i<4;i++)
	{
		cout<<*ptr<<"\t";
		ptr++;
	}
	cout<<"\n\t\t\t---------------------------------------------\n";
	cout<<"\t\t\t*****************    ********  *************\n";
}
return 0;
}

