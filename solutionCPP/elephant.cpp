#include <iostream>
#include <cmath>
using namespace std;

int main()
{

    int num;
    //int num;
    cin >> num;
    for (int i = 0; i != -1; i++)
    {

        //num = num - 5;
        //cout << num << endl;
        if (num - 5 > 0)
        {
            num = num - 5;
        }
        else if (num - 4 > 0)
        {
            num = num - 4;
        }
        else if (num - 3 > 0)
        {
            num = num - 3;
        }
        else if (num - 2 > 0)
        {
            num = num - 2;
        }
        else if (num - 1 > 0)
        {
            num = num - 1;
        }
        else if (num == 0)
        {
            cout << i << endl;
            break;
        }
    }

    return 0;
}