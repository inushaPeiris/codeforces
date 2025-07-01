#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;
    int res = a % 2; 

    if (res == 0 && a >= 4) {
        cout << "YES";
    } else {
        cout << "NO";
    };

    return 0;
}
