#include <iostream>
using namespace std;
 class stack{
	private:
		int top;
		int array[5];
		public:
	stack()
	{
		top=-1;
		for(int i=0;i<=4;i++)
		{
			array[i]=0;
		}
	}

   void push(int pushvalue)
   {
	   
	   	top++;
	   	array[top]=pushvalue;
	   
   }
   int pop()
   {
	   	int popvalue=array[top];
	   	array[top]=0;
	   	top--;
	   	return popvalue;
	
   }
   void display()
   {
   	for(int i=4;i>=0;i--)
   	{
   		cout<<array[i]<<"\t";
	   }
	   cout<<endl;
   }
};
   main()
   {
   	stack s1;
   	int option,position,value;
   	do{
   		cout<<"select stack operation,enter 0 for exit"<<endl;
   		cout<<"1.push"<<endl;
   		cout<<"2.pop"<<endl;
   		cout<<"3.display"<<endl;
   		cin>>option;
	   
   
   
   switch(option)
   {
   	case 1:
   		cout<<"enter any value to push"<<endl;
   		cin>>value;
   		s1.push(value);
   		break;
   		case 2:
   			cout<<"pop function called \n pop value"<<s1.pop();
   			break;
   		case 3:
		   s1.display();
		   break;
		   default:
		   cout<<"invalid operation"<<endl;	
   		}
   }
   while(option!=0);
}
