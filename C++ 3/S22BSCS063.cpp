#include<iostream>

using namespace std;

int main()
{


int n[5];
int i;
for (i=0;i<5;i++)
{
	
	cout<<"please enter the element number "<<i+1<<":";
	cin>>n[i];
	
}
cout<<endl;

for(i=0; i<5;i++)
{

cout<<"element stored at index "<<i<<" is:"<<n[i]<<endl;
}
 return 0;

}
