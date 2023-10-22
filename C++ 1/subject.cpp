#include<iostream>
using namespace std;
main()
{
	int physics,chemistry,biology,mathematics,programming,obtainmark,totalmark,percentage;
	totalmark=500;
	cout<<"Enter physics marks="<<endl;
	cin>>physics;
	cout<<"Enter chemistry marks="<<endl;
	cin>>chemistry;
	cout<<"Enter biology marks="<<endl;
	cin>>biology;
	cout<<"Enter mathematics marks="<<endl;
	cin>>mathematics;
	cout<<"Enter programming marks="<<endl;
	cin>>programming;
	obtainmark=physics+chemistry+biology+mathematics+programming;
	cout<<obtainmark<<endl;
	percentage=obtainmark*100/totalmark;
	cout<<"percentage="<<percentage<<endl;
	if(percentage>=90)
	{
		cout<<"Grade A"<<endl;
	}
	else if(percentage>=80)
	{
		cout<<"Grade B"<<endl;
	}
	else if(percentage>=70)
	{
		cout<<"Grade C"<<endl;
	}
	else if(percentage>=60)
	{
		cout<<"Grade D"<<endl;
	}
	else if(percentage>=50)
	{
		cout<<"Grade E"<<endl;
	}
	else if(percentage>90>=40)
	{
		cout<<"congratulations you are pass"<<endl;
	}
	else
	{
		cout<<"Grade Fail";
	}
}
