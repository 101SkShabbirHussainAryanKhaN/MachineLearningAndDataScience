#include <iostream>
using namespace std;
main()
{
	int num2;
	num2=5;
	++num2;
	cout<<"num2"<<endl;
	float a , b , c , d , solution;
	cout<<"enter four integers"<<endl;
	cin>>a>>b>>c>>d;
	solution=a*(b+c*d)+ ++num2;
	cout<<"solution="<<solution;
}
