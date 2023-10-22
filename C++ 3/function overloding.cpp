  
  #include <iostream>
using namespace std;
//int sum (int a ,int b){
//	return a+b;
//}
//float sum(float x, int y, int z){
//	return x+y+z;
//}
//int main(){
//	cout<<"sum of a & b :"<<sum(4, 7)<<endl;
//	cout<<"sum of x, y :"<<sum(1.3, 5,6);
//return 0;
//}
int sum(double a, int b){
	return a+b;
}
float sum(double a, double b){
	return a+b;
}
int sum(int a, int b){
	return a+b;
}
float sum(int a, double b){
	return a+b;
}
int main (){
	cout<<"sum is :"<<sum(2.5, 3)<<endl;
	cout<<"sum is :"<<sum(2.5, 2.5)<<endl;
	cout<<"sum is :"<<sum(2, 2)<<endl;
	cout<<"sum is :"<<sum(3, 2.5)<<endl;
}
