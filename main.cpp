//      **************************************************
//      Find the min, max among three values
//      Display three values in ascending order  min, other, max
//     **************************************************
#include <iostream>
using namespace std;
int main()
{
    int num1, num2, num3;
    int min, max, med;
    cout << "Enter three integer values: ";
    cin >> num1 >> num2 >> num3;

    // TODO: Find min, max, and med among num1, num2, num3
    // Determine min
    if (num1 <= num2 && num1 <= num3)
        min = num1;
    else if (num2 <= num1 && num2 <= num3)
        min = num2;
    else
        min = num3;

    // Determine max
    if (num1 >= num2 && num1 >= num3)
        max = num1;
    else if (num2 >= num1 && num2 >= num3)
        max = num2;
    else
        max = num3;

    // Determine med (the remaining value)
    if (num1 != min && num1 != max)
        med = num1;
    else if (num2 != min && num2 != max)
        med = num2;
    else
        med = num3;
    // END TODO

    cout << min << " " << med << " " << max << endl;
}
