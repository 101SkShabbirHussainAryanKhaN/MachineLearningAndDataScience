#include<iostream>
#include<ctype.h>
using namespace std;
int main(){
	int array[5];
	int i,elem;
	cout<<"Enter the array : "<<endl;
	for(i=0;i<5;i++)
	cin>>(array[i]);
	cout<<"Enter element to insert : ";
	gets (elem);
	array[i]=elem;
	cout<<"The new array is : ";
	for(i=0;i<6;i++)
	cout<<array[i]<<" ";
	cout<<endl;
	return 0;
}

