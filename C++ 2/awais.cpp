#include<iostream>
#include<ctype.h>
using namespace std;
int main(){
	cout<<"According to isdigit():\n";
	isdigit('8') ? cout<<"Digit": cout<<"not digit";
	cout<<endl;
	isdigit('#') ? cout<<"Digit": cout<<"not digit";
	cout<<endl;
	cout<<"According to isalpha():\n";
	isalpha('A') ? cout<<"letter":cout<<"not letter";
	cout<<endl;
	isalpha('B') ? cout<<"letter":cout<<"not letter";
	cout<<endl;
	isalpha('&') ? cout<<"letter":cout<<"not letter";
	cout<<endl;
	isalpha('4') ? cout<<"letter":cout<<"not letter";
	cout<<endl;
	return 0;
	
	
}
