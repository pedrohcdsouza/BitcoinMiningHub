#include <iostream>

int main(){
    int A, B;
    std::cin >> A >> B;

    if(A%B == 0){
        std::cout << "It's " << (A/B) + 1 << " lights.";
    }   else {
        std::cout << "It's " << (A/B) + 2 << " lights.";
    }

    return 0;
}