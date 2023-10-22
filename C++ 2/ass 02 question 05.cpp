#include<iostream>
using namespace std;
main()
{
int year;
cout<<"Enter the year \t"<<endl;
cin>>year;
switch (year%4==0&&year/100!=0)
{
case 1:
cout<<"This is a leap year";
break;
default:
cout<<"This is not a leap year";
}

}

