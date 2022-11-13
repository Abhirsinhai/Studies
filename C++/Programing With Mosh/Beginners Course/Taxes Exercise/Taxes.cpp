#include <iostream>

using namespace std;

int main() {
    int Sales = 95000;
    float StateTax = Sales * .04;
    float CountyTax = Sales * .02;
    cout << "Sales = " + Sales << endl;
    cout << "State Tax = " + StateTax << endl;
    cout << "County Tax = " + CountyTax << endl;

    return 0;
}