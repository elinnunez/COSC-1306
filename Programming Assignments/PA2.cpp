// Elinnoel Nunez
// Program #2: The Trig Calculator in C++
// COSC 1306
// Spring 2021
// Calculates sin, cos, tan of an angle given in degree into radians

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int factorial(int num)
{
    if (num < 1)
    {
        return 1;
    }
    else
    {
        return num * factorial(num - 1);
    }
}

double sin(double num, int terms)
{

    double value = num;

    int constant, denominator;
    double numerator, cur;

    for (int n = 1; n < terms; n++)
    {
        constant = pow(-1, n);
        numerator = pow(num, (2 * n) + 1);
        denominator = factorial((2 * n) + 1);
        cur = (numerator / denominator) * constant;
        value += cur;
    }

    return value;
}

double cos(double num, int terms)
{
    double value = 1;

    int constant, denominator;
    double numerator, cur;

    for (int n = 1; n < terms; n++)
    {
        constant = pow(-1, n);
        numerator = pow(num, 2 * n);
        denominator = factorial(2 * n);
        cur = (numerator / denominator) * constant;
        value += cur;
    }

    return value;
}

double degTorad(int value)
{
    double pi = 2 * acos(0.0);
    double result = value * pi / 180;

    return result;
}

void printMenu()
{
    cout << "THE TRIGONOMETRIC CALCULATOR" << endl;
    cout << "1 - Calculate the sine of a value" << endl;
    cout << "2 - Calculate the cosine of a value" << endl;
    cout << "3 - Calculate the tangent of a value" << endl;
    cout << "4 - Exit" << endl;
}

bool isNumeric(string str)
{
    for (int i = 0; i < str.length(); i++)
        if (isdigit(str[i]) == false)
            return false; //when one non numeric value is found, return false
    return true;
}

int main()
{

    string option = "str";

    while (option != "4")
    {
        printMenu();
        cout << "Enter your option: ";
        cin >> option;

        if (isNumeric(option) == true)
        {
            if (0 < stoi(option) && stoi(option) < 4)
            {
                int value;
                int terms;
                double result;

                cout << "Enter the value (in degrees): ";
                cin >> value;
                cout << "Enter the number of terms: ";
                cin >> terms;
                double radians = degTorad(value);

                if (stoi(option) == 1)
                {
                    result = sin(radians, terms);
                    cout << "The sine of " << value << " is " << result << endl;
                }
                else if (stoi(option) == 2)
                {
                    result = cos(radians, terms);
                    cout << "The cosine of " << value << " is " << result << endl;
                }
                else if (stoi(option) == 3)
                {
                    if (value == 90 || value == 270)
                    {
                        cout << "The tangent of " << value << " is undefined" << endl;
                    }
                    else
                    {
                        result = sin(radians, terms) / cos(radians, terms);
                        cout << "The tangent of " << value << " is " << result << endl;
                    }
                }
            }
            else if (stoi(option) == 4)
            {
                break;
            }
            else
            {
                cout << "Invalid Option: Please Try Again!" << endl;
            }
        }
        else
        {
            cout << "Invalid Option: Please Try Again!" << endl;
        }
    }

    return 0;
}