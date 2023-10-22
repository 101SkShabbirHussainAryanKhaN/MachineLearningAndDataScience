#include<iostream>
using namespace std;
main()
{
    int n, reverse = 0, remainder;

    cout << "Enter any number: ";
    cin >> n;

    while(n != 0)
    {
        remainder = n%10;
        reverse = reverse*10 + remainder;
        n /= 10;
    }

    cout << "Reverse Number = " << reverse;

}

