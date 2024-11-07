#include <iostream>

int main() {

    int a, d;

    std::cin >> a;

    d = 0;

    for(int v = 1; v < a; v = v*2){
        d = d + 1;
    }

    std::cout << d;

    return 0;
}