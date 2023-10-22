#include<iostream>
using namespace std;
main()
{
	int i,n;
	cout<<"Enter number\n";
	cin>>n;
	int N=2*n;
	for(i=1;i<=N;i++)
	{
		if(i%2==0)
		cout<<i<<",";
	}
	int sum=	n*(n+1);
	cout<<"\nSum of "<<n<<" even number="<<sum;
}

