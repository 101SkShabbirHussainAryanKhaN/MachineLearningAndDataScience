#include<iostream>
using namespace std;
main()
{
    int MonthNumber;
    cout<<"Enter month number (1-12):\n";
    cin>>MonthNumber;
    switch (MonthNumber)
    {  case 1:
        cout<<"January: has 31 days  \n";
         break;
         
        case 2:
        cout<<"February:has 28 days \n";
        break;
        
        case 3:
        cout<<"March:has 31 days\n";
        break;
        
        case 4:
        cout<<"April:has 30 days\n";
        break;
        
        case 5:
        cout<<"May:has 31 days\n";
        break;
        
        case 6:
        cout<<"June:has 30 days\n";
        break;
        
        case 7:
        cout<<"July:has 31 days\n";
        break;
        
        case 8:
        cout<<"August:has 31 days\n";
        break;
        
        case 9:
        cout<<"September:has 30 days\n";
        break;
        
        case 10:
        cout<<"October:has 31 days\n";
        break;
        
        case 11:
        cout<<"November:has 30 days\n";
        break;
        
        case 12:
        cout<<"December:has 31 days\n";
        break;
        default:
        cout<<" you entered invalid Month numbar";
        }
}

