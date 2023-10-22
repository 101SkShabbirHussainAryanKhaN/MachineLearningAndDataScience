#include<iostream>
using namespace std;
main()
{
	string Bloodgroup;
	cout<<"Enter your blood group"<<endl;
	cin>>Bloodgroup;
	cout<<"you can donate blood to:-"<<endl;
	if(Bloodgroup=="O-"||Bloodgroup=="o-")
	{
		cout<<"AB+\t AB-\t A+\t A-\t B+\t B-\t O+\t O-\t"<<endl;
	}
	else if(Bloodgroup=="O+"||Bloodgroup=="o+")
	{
		cout<<"AB+\t A+\t B+\t O+\t"<<endl;
	}
	else if(Bloodgroup=="B-"||Bloodgroup=="b-")
	{
		cout<<"AB+\t AB-\t B+\t B-\t"<<endl;
	}
	else if(Bloodgroup=="B+"||Bloodgroup=="b+")
	{
		cout<<"AB+\t B+\t"<<endl;
	}
	else if(Bloodgroup=="A-"||Bloodgroup=="a-")
	{
		cout<<"AB+\t AB-\t A+\t A-\t"<<endl;
	}
	else if(Bloodgroup=="A+"||Bloodgroup=="a+")
	{
		cout<<"AB+\t A+\t"<<endl;
	}
	else if(Bloodgroup=="AB-"||Bloodgroup=="ab-")
	{
		cout<<"AB+\t AB-\t"<<endl;
	}
	else if(Bloodgroup=="AB+"||Bloodgroup=="ab+")
	{
		cout<<"AB+"<<endl;
	}
	else
	{
		cout<<"you entered invalid Group"<<endl;
	}
	}
