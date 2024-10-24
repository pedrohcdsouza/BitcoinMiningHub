#include <iostream>

int main() {

    int A, B, C;
    bool Verify = true;

    std::cin >> A >> B;

    C = A > B ? A : B;

    for (int i = 2; i < C; i++){
        if(A % i == 0 || B % i == 0){
            Verify = false;
            break;
        }

    }

    std::cout << Verify;

    return 0;
    
}