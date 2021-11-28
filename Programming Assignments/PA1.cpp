// Elinnoel Nunez
// Program #1: The Area Calculator
// COSC 1306 in C++
// Spring 2021
// Calculates area based on shape chosen from list. (square, rectange, triangle)

// Probably fix invalid inputs for base/height/length/width variables in loop --- FIXED

#include <iostream>
#include <string>

using namespace std;

bool isNumeric(string str)
{
    for (int i = 0; i < str.length(); i++)
        if (isdigit(str[i]) == false)
            return false; //when one non numeric value is found, return false
    return true;
}

int main()
{
    cout << "Select a figure from the menu: " << endl;
    cout << "1 - Square" << endl;
    cout << "2 - Rectangle" << endl;
    cout << "3 - Triangle" << endl;

    int selection;
    cout << "Enter your selection: ";
    cin >> selection;

    if (selection == 1)
    {
        string base = "str";

        while (isNumeric(base) != true)
        {
            cout << "Enter the side length: ";
            cin >> base;
        }

        int area = stoi(base) * stoi(base);
        cout << "The area of the selected figure is: " << area << endl;
    }
    else if (selection == 2)
    {
        string length = "str";
        string width = "str";

        while (isNumeric(length) != true || isNumeric(width) != true)
        {
            if (isNumeric(length) == false)
            {
                cout << "Enter the length of the rectangle: ";
                cin >> length;
            }
            else
            {
                cout << "Enter the width of the rectangle: ";
                cin >> width;
            }
        }

        cout << "The area of the selected figure is: " << stoi(length) * stoi(width) << endl;
    }
    else if (selection == 3)
    {
        string base = "str";
        string height = "str";

        while (isNumeric(base) != true || isNumeric(height) != true)
        {
            if (isNumeric(base) == false)
            {
                cout << "Enter the base of the triangle: ";
                cin >> base;
            }
            else
            {
                cout << "Enter the height of the triangle: ";
                cin >> height;
            }
        }

        int area = (stoi(base) * stoi(height)) / 2;
        cout << "The area of the selected figure is " << area << endl;
    }
    else
    {
        cout << "Invalid Option" << endl;
    }

    return 0;
}