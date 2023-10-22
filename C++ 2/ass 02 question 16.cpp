#include<iostream>
using namespace std;
main()
{
	int Units;
	float TotalBill;
	float extrapercent,Bill;
	cout<<"Enter total units\n";
	cin>>Units;
	if(Units>=0&&Units<=50)
	{
	Bill=Units*0.50;
extrapercent=Bill*20/100;
TotalBill=extrapercent+Bill;
cout<<"TotalBill=RS"<<TotalBill;
	
	}
else if(Units>50&&Units<=150)
{
	Bill=Units*0.75;
extrapercent=Bill*20/100;
TotalBill=extrapercent+Bill;
cout<<"TotalBill=RS"<<TotalBill;
	
	}
else if(Units>150&&Units<=250)
	{
	Bill=Units*1.20;
extrapercent=Bill*20/100;
TotalBill=extrapercent+Bill;
cout<<"TotalBill=RS"<<TotalBill;
	
	}
else if(Units>250)
	{
	Bill=Units*1.50;
extrapercent=Bill*20/100;
TotalBill=extrapercent+Bill;
cout<<"TotalBill=RS"<<TotalBill;
	
	}	
else
	cout<<"Invalid Unit\n";

}

