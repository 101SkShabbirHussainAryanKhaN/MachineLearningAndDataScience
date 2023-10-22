#include<iostream>
using namespace std;
main()
{
	float age,height;
	cout<<"Enter your Age="<<endl;
	cin>>age;
	cout<<"Enter your Height="<<endl;
	cin>>height;
	if(age>=18||height>=6)
	{
	cout<<"congratulations:you are eligible for this post";
}
else
{
	cout<<"oops:sorry you are not eligible for this post";
}
}
