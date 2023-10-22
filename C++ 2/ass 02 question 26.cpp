#include<iostream>
using namespace std;
main()
{
int i,n;
	cout<<"enter any number \n";
	cin>>n;
	cout<<"Sum of "<<n<<" odd number is \n";
	int N=2*n-1;
	for(i=0;i<=N;i++)
	{
		if(i%2!=0)
		cout<<i<<"+";
	}
	cout<<"\b="<<n*n;

}

