#include <iostream>
#include <string.h>
using namespace std;
#define maxSize 100
int main()
{
	char text [maxSize];
	int lenght;
	cout<<"Enter any String :\n";
	gets(text);
	cout<<text;
	lenght=strlen(text);
	cout<<"\nyour string lenght is :"<<lenght;
return 0;
}

