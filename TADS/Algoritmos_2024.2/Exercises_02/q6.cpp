#include <iostream>

int main() {

    int A;
    bool Verify = true;

    std::cin >> A;

    for(int i = 2; i < A; i++){

        if(A%i == 0){
            Verify = false;
            break;
        }

    }

    std::cout << Verify; // 0 -> false; 1 -> true;

    return 0;
}