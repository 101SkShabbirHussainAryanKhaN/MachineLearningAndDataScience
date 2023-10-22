#include<iostream>
using namespace std;
int main()
{
	float angleA,angleB,angleC,sumOfAngle;
	cout<<"enter first angle\n ";
	cin>>angleA;
	cout<<"enter Second angle\n";
	cin>>angleB;
	cout<<"enter third angle\n";
	cin>>angleC;
	sumOfAngle=(angleA+angleB+angleC);
	if(	sumOfAngle==180)
	{
		cout<<" the triangle is valid ";
	}
	else
	cout<<"invalid triangle";
return 0;
}

