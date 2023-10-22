#include <iostream>
#include <ctype.h>
using namespace std;
int main()
{
	cout<<"-----------------------------------------------\n";
	cout<<"**************     *****    *******************\n";
	//program to check whether a Digit or not:
	
	cout<<"According to is digit():\n";
	isdigit('8')?cout<<"\nDigit ":cout<<"not Digit";
	cout<<endl;
	
	isdigit('#')?cout<<"Digit ":cout<<"not DIgit";
	cout<<endl;
	
	cout<<"-----------------------------------------------\n";
	cout<<"**************     *****    *******************\n";
	//program to check whether a letter or not:
	
	cout<<"According to is Alpha():\n";
	isalpha('A')?cout<<"\nLetter ":cout<<"not letter";
	cout<<endl;

	isalpha('b')?cout<<"Letter ":cout<<"not letter";
	cout<<endl;
	
	isalpha('&')?cout<<"Letter ":cout<<"not letter";
	cout<<endl;
	
	isalpha('4')?cout<<"Letter ":cout<<"not letter";
	cout<<endl;
	
	cout<<"-----------------------------------------------\n";
	cout<<"**************     *****    *******************\n";
	//program to check whether a hexa decimal digit or not:
	
	cout<<"According to is xdigit():\n";
	isxdigit('F')?cout<<"\nhexadecimal Digit ":cout<<"not hexadecimal Digit";
	cout<<endl;
	
	isxdigit('j')?cout<<"hexadecimal Digit ":cout<<"not hexadecimal Digit";
	cout<<endl;
	
	isxdigit('7')?cout<<"hexadecimal Digit ":cout<<"not hexadecimal Digit";
	cout<<endl;
	
	isxdigit('$')?cout<<"hexadecimal Digit ":cout<<"not hexadecimal Digit";
	cout<<endl;
	
	isxdigit('f')?cout<<"hexadecimal Digit ":cout<<"not hexadecimal Digit";
	cout<<endl;
	
	cout<<"-----------------------------------------------\n";
	cout<<"**************     *****    *******************\n";
return 0;
}

