#include<iostream>
using namespace std;
main()
{
	int age1,age2,age3,age4,age5;
	cout<<"enter the age of students="<<endl;
	cin>>age1;
	cin>>age2;
	cin>>age3;
	cin>>age4;
	cin>>age5;
	if(age1>age2&&age1>age3&&age1>age4&&age1>age5)
	{
		cout<<"ag1 is the oldest student"<<endl;
	}
	else if(age2>age1&&age2>age3&&age2>age4&&age2>age5)
	{
		cout<<"age2 is the oldest student"<<endl;
	}
	else if(age3>age1&&age3>age2&&age3>age4&&age3>age5)
	{
		cout<<"age3 is the oldest student"<<endl;
	}
	else if(age4>age1&&age4>age2&&age4>age3&&age4>age5)
	{
		cout<<"age4 is the oldest student"<<endl;
	}
	else
	{
		cout<<"age5 is the oldest student"<<endl;
	}
	if(age1<age2&&age1<age3&&age1<age4&&age1<age5)
	{
		cout<<"age1 is the youngest student"<<endl;
	}
		else if(age2<age1&&age2<age3&&age2<age4&&age2<age5)
	{
		cout<<"age2 is the youngest student"<<endl;
	}
		else if(age3<age1&&age3<age2&&age3<age4&&age3<age5)
	{
		cout<<"age3 is the youngest student"<<endl;
	}
		else if(age4>age1&&age4>age2&&age4>age3&&age4>age5)
	{
		cout<<"age4 is the youngest student"<<endl;
	}
	else
	{
		cout<<"age5 is the youngest student";
	}
}
