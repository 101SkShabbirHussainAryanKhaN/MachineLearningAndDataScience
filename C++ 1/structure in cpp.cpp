#include <iostream>
using namespace std;
struct person
{
	char name[50];
	char cnic[15];
	int age;
	float salary;
}p1, p2, p3;
int main(){
	cout<<"enter  name of person :";
	cin.getline(p1.name,50);
	cout<<"\nenter  name cnic of person :";
	cin.getline(p1.cnic,15);
	cout<<"\nenter  age of person :";
	cin>>p1.age;
	cout<<"\nenter  name of person :";
	cin>>p1.salary;
	
return 0;
}

