#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
    int a = 0;
    int b = 0;
    int &ra = a;
    int &rb = b;
    t = ra;ra=rb;rb=t;
    cout << a << endl;
    return 0;
}