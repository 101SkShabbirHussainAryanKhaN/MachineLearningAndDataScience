#include<iostream>
using namespace std;
int main()
{
	int y[10]={1,2,3,4,5,6,7,8,9,10};
	int *yptr=y;
	yptr=y;
	cout<<"\t\t\t--------------------------------------------\n";
	cout<<"\t\t\t*****************    ********  *************\n";
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	yptr++;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	*yptr+4;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	*yptr=*yptr+4;
	cout<<"\t\t\tadress : "<<yptr<<" \t|\tValue : "<<*yptr<<endl;
	cout<<"\t\t\t---------------------------------------------\n";
	cout<<"\t\t\t*****************    ********  *************\n";

	
return 0;
}

