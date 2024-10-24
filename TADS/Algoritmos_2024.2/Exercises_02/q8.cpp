#include <iostream>

int main() {
     
    int a, b, c, max;
    std::cin >> a >> b;

    max = 0;

    c = a > b ? a: b;

    for(int i = 1; i < c; i++){
        if(a % i == 0 & b % i == 0){
            max = i;
            }
    }
    

    std::cout << max;
    
    return 0;
}