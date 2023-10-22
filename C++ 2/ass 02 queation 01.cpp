#include<iostream>
using namespace std;
main()
{
int physics,chemistry,biology,mathematics,programming,obtainmark,totalmark;
	float percentage;
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
	cout<<"obtainmark = "<<obtainmark<<endl;
	percentage=obtainmark*100/totalmark;
	cout<<"percentage = "<<percentage<<endl;
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
	else if(percentage>=40)
	{
		cout<<"Grade E"<<endl;
	}
	else if(percentage<40)
	{
		cout<<"Grade F"<<endl;
	}
	else
	{
		cout<<"Fail";
	}

}

