#include <iostream>
#include <string>
using namespace std;

int main(){
    string a;
    int b(0), c(0);
    cin >> a;
    for(int i = 0; i < a.size(); i++){
        if(a[i] >= 'a' && a[i] <= 'z'){
            b++;
        }else if(a[i] >= 'A' && a[i] <= 'Z'){
            c++;
        }
    }
    cout << b << ' ' << c << endl;
}