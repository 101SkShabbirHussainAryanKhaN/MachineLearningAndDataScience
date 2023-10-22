

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
// This is my first Project where I try to Arrange Quiz competition
// here I ask fifteen question where we give there anwser and score marks....
// total marks are fifteen  
// after in quiz competition you see your marks...

#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int option,score=0;
	string First_Name,Second_Name;
	char ch,op;
	system("color 5f");
	
	// this is front page of this project:
	cout<<"\t\t=========================\n";
	cout<<"\t\t****WelcOme to Quiz Game****\n";
	cout<<"\t\t=========================\n";
	cout<<"\t\t***Developers:- Sahbbir Hussain Aryan Khan ***\n";
	cout<<"\t\t***Developers:- Shakir Ali AKbar***\n";
	cout<<"\t\t=========================\n";

// space are not allowed in your name donnot give blank space in your name write your name as ShanAli:

	cout<<"\t\tEnter Your First Name:";
	cin>>First_Name;
	cout<<"\t\tEnter Your Second Name:";
	cin>>Second_Name;
	cout<<"\n";
	
	cout<<"\t\tWelcome\t"<<First_Name<<"\t"<<Second_Name<<" to our Quiz competition world:"<<endl;
	getch();
	system("cls");
	
	main:
		
	// this is also front page of this project:
	
	cout<<"\n\t\t1)Start Quiz:\n";
	cout<<"\n\t\t2)View Score:\n";
	cout<<"\n\t\t3)Quit Game:\n";
	
	cout<<"\n\t\tSelect one option frOm above=\n";
	
	cin>>option;
	while(option<1 || option>3)
	{
		cout<<"Please! Enter valid number from(1-3):";
		cin>>option;
	}
	
	switch(option)
	{
		case 1:
			system("color 1f");
		// Question number 01
		
		cout<<"\t\t\nQ1-Who is the first prime minister of pakistan?\n";
		
		cout<<"\t\tA.Quaid e Azam\n";
		cout<<"\t\tB.Nazim uddin\n";
		cout<<"\t\tC.Ali Bogra\n";
		cout<<"\t\tD.Liaqat Ali Khan\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		// putting condition 
		
		if(ch=='d' or ch=='D')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
//			question number 02

		cout<<"\t\t\nQ 02-Which city known as brazilia of pakistan?\n";
		
		cout<<"\t\tA.faisalabad\n";
		cout<<"\t\tB.Islamabad\n";
		cout<<"\t\tC.D.I khan\n";
		cout<<"\t\tD.Peshawar\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='b' or ch=='B')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
		// Question number 03
		
		cout<<"\t\t\nQ 03-Which first country who accept pakitan as coutry after independence?\n";
		
		cout<<"\t\tA.Egypt\n";
		cout<<"\t\tB.Afghanistan\n";
		cout<<"\t\tC.Iran\n";
		cout<<"\t\tD.Saudi Arabia\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='c' or ch=='C')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
				// Question number 04
				
		cout<<"\t\t\nQ 04-Which is longest river of pakistan?\n";
		
		cout<<"\t\tA.Ravi river\n";
		cout<<"\t\tB.Indus river\n";
		cout<<"\t\tC.Chenab river\n";
		cout<<"\t\tD.Jehlum river\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='b' or ch=='B')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
			// Question number 05
			
		cout<<"\t\t\nQ 05-who is the first president of Pakistan?\n";
		
		cout<<"\t\tA.Sikandar Mirza\n";
		cout<<"\t\tB.Quaid E Azam\n";
		cout<<"\t\tC.Muhammad Ali johar\n";
		cout<<"\t\tD.Sardar Abdul Rab Nashtar\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='a' or ch=='A')
		{
			cout<<"\n\t\t.Correct option \n\n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
		
		// Question number 06
		
		cout<<"\t\t\nQ 06-Which city known as the city of Perfumes?\n";
		
		cout<<"\t\tA.Islamabad\n";
		cout<<"\t\tB.Peshawar\n";
		cout<<"\t\tC.Haiderabad\n";
		cout<<"\t\tD.Multan\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='c' or ch=='C')
		{
			cout<<"\n\t\t.Correct option \n\n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
	    // Question number 07
	    
	    cout<<"\t\t\nQ 07-Which is the coldest place of Pakistan ?\n";
	    
		cout<<"\t\tA.Islamabad\n";
		cout<<"\t\tB.Skardu the Great city\n";
		cout<<"\t\tC.Quetta\n";
		cout<<"\t\tD.Ziyarat\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='b' or ch=='B')
		{
			cout<<"\n\t\t.Correct option \n\n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
		// Question number 08
		
		cout<<"\t\t\nQ 08-Which city is known as city of lights?\n";
		
		cout<<"\t\tA.Sukhur\n";
		cout<<"\t\tB.Peshawar\n";
		cout<<"\t\tC.Karachi\n";
		cout<<"\t\tD.Multan\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='c' or ch=='C')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
		// Question number 09
		
		cout<<"\t\t\nQ 09-Which is the oldest city of Pakistan?\n";
		
		cout<<"\t\tA.Sukhur\n";
		cout<<"\t\tB.Peshawar\n";
		cout<<"\t\tC.Karachi\n";
		cout<<"\t\tD.Multan\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='d' or ch=='D')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
		// Question number 10
		
		cout<<"\t\t\nQ 10-Where is the national musseum of Pakistan?\n";
		
		cout<<"\t\tA.Sukhur\n";
		cout<<"\t\tB.Peshawar\n";
		cout<<"\t\tC.Karachi\n";
		cout<<"\t\tD.Multan\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='c' or ch=='C')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
			// Question number 11
		
		cout<<"\t\t\nQ 11-What is the national Game of Pakistan?\n";
		
		cout<<"\t\tA.Cricke\n";
		cout<<"\t\tB.Hockey\n";
		cout<<"\t\tC.Football\n";
		cout<<"\t\tD.Tennis\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='b' or ch=='B')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
				// Question number 12
		
		cout<<"\t\t\nQ 12-What is the duration of national anthem of Pakistan?\n";
		
		cout<<"\t\tA.One minute\n";
		cout<<"\t\tB.One minute ten seconds\n";
		cout<<"\t\tC.One minute twenty seconds\n";
		cout<<"\t\tD.One minute thirty seconds\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='c' or ch=='C')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
				// Question number 13
		
		cout<<"\t\t\nQ 13-Who wrote the national anthem of Pakistan?\n";
		
		cout<<"\t\tA.Hafiz Jalandhari\n";
		cout<<"\t\tB.Allam Iqbal\n";
		cout<<"\t\tC.Chaudary Rehmat Ali\n";
		cout<<"\t\tD.Liaqat ALi Khan\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='a' or ch=='A')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
				// Question number 14		
		cout<<"\t\t\nQ 14-What is the national flower of Pakistan?\n";
		
		cout<<"\t\tA.Rose\n";
		cout<<"\t\tB.Jasmin\n";
		cout<<"\t\tC.Sun Flower\n";
		cout<<"\t\tD.Lilly Flower\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='b' or ch=='B')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
				// Question number 15
		
		cout<<"\t\t\nQ 15-When was the all India Muslim league established?\n";
		
		cout<<"\t\tA.1880\n";
		cout<<"\t\tB.1885\n";
		cout<<"\t\tC.1906\n";
		cout<<"\t\tD.1913\n";
		
		cout<<"\n\t\tEnter the correct option=";
		cin>>ch;
		
		if(ch=='c' or ch=='C')
		{
			cout<<"\n\t\t.Correct option \n";
			score=score+1;
			}
			else
			{
				cout<<"\t\tx.Sorry! wrong answer\n";
				}
				
	cout<<"\n\t\t1)Start Quiz:\n";
	cout<<"\t\t2)View Score:\n";
	cout<<"\t\t3)Quit Game:\n";
	cout<<"\n\t\tSelect one option frOm above=";
	cin>>option;
		while(option<1 || option>3)
	{
		cout<<"Please! Enter valid number from(1-3):";
		cin>>option;
	}
		
		case 2:
			system("color 2f");
		cout<<"\n\t\tTotal score=15\n\n";
		
		cout<<"\n\t\tObtain Score is="<<score<<"\n";
		
	cout<<"\n\t\t1)Start Quiz:\n";
	cout<<"\n\t\t2)View Score:\n";
	cout<<"\n\t\t3)Quit Game:\n";
	
	cout<<"\n\t\tSelect one option frOm above=";
	cin>>option;
	
		while(option<1 || option>3)
	{
		
		cout<<"Please! Enter valid number from(1-3):";
		cin>>option;
	}
	
		break;
		
		case 3:
		system("color 4f");	
		cout<<"\n\t\tDo you want to exit the Quiz(y/n)=";
		cin>>op;
		
		if(op=='y' or op=='Y')
		{
		break;
		}
		else
		{
			goto main;
		}
		break;
	}
}


