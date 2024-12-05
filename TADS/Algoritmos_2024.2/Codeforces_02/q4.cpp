#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    
    int a;
    std::cin >> a;

    int b[a], c[a];

    for (int i = 0; i < a; i++) {
        std::cin >> b[i];
        if (b[i] == 0) {
            c[i] = 0;
        }
    }

    for (int i = 1; i < a; i++) {
        if (c[i] != 0) {
            c[i] = std::min(c[i], c[i - 1] + 1);
        }
    }

    for (int i = a - 2; i >= 0; i--) {
        if (c[i] != 0) {
            c[i] = std::min(c[i], c[i + 1] + 1);
        }
    }

    for (int i = 0; i < a; i++) {
        if (c[i] > 9) {
            c[i] = 9;
        }
        std::cout << c[i] << " ";
    }

    return 0;
    
}