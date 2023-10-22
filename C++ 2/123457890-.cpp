#include <iostream>
using namespace std;
int arr(int arr[],int);
int main()
{
	int arr[10]={3,5,2,12,16,1,6,8,7,9};
	
return 0;
}
int arr(int arr[],int j);
int j=0;
{
for(int i=0;i<=10;i++)
{
  if(arr[i]>j)
  {
j=arr[i];
}

}
cout<<j;
}
