#include<iostream>
using namespace std;
int main(){
	int array[5],tota=5;
	int i,j,elem;
	int found=0;
	cout<<"Enter the array elements "<<endl;
	for(i=0;i<tota;i++)
	cin>>array[i];
	cout<<"Enter elements to delete ";
	cin>>elem;
	for(i=0;i<tota;i++)
	{
		if(array[i]==elem){
			for(j=i;j<(tota-1);j++)
			array[j]=array[j+1];
			found++;
			i--;
			tota--;
		}
		}	
		if(found==0)
		cout<<"Elements does not found in the array ";
		else
		cout<<"Element delete successfully ";
		cout<<endl;
		return 0;
}

