#include<iostream>
using namespace std;
main()
{
	char ch;
cout<<"Enter any Aphabet\t"<<endl;
cin>>ch;
if(ch>='a' && ch<='z')
{
cout<<ch<<":is lower case alphabet";
}
else if(ch>='A' && ch<='Z')
{
cout<<ch<<":is upper case Alphabet";
}
else
{
cout<<"you entered invalid character";
}

}

