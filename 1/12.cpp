#include <iostream>
using namespace std;

void hot(int n) {
    if (n == 0) return;
    cout << n % 10;
    if (n / 10 > 0) cout << " ";
    hot(n / 10);
}

int main() {
    int n;
    cin >> n;
    hot(n);
    return 0;
}