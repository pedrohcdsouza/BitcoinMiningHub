#include <iostream>

char SumOfPair(int S){
    int A[8] = {10, 20, 9, 1, 63, 6, 5, 12};

    for (int i = 0; i < 8; i++) {
        for (int j = i + 1; j < 8; j++) {
            if (A[i] + A[j] == S) {
                return 'S';
            }
        }
    }
    return 'N';
}

int main(){
    char result = SumOfPair(2);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
