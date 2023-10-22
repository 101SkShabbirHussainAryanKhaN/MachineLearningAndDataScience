#include <iostream> 
using namespace std;
main()
{
	int num1, num2, num3, num, solution;
	cout<<"enter the first number"<<endl;
	cin>>num1;
	cout<<"enter the 2nd number"<<endl;
	cin>>num2;
	num2++;
	cout<<"num2"<<endl;
	cout<<"enter the 3rd number"<<endl;
	cin>>num3;
	cout<<"enter the 4th number"<<endl;
	cin>>num;
	
	solution=num1+num2/num3+num+num2++;
	cout<<"the solution of the equation is="<<solution<<endl;
}
