#include<iostream>
using namespace std;
main()
{
    int n, SumDigitNumber = 0, remainder;

    cout << "Enter any number: ";
    cin >> n;

    while(n != 0)
    {
        remainder = n%10;
        SumDigitNumber+= remainder;
        n /= 10;
    }

    cout << "sum of the digit of number = " <<SumDigitNumber;

}

