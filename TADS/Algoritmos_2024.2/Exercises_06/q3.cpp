#include <iostream>

char RightTriangle(int b, int A[]){
    for(int i = 0; i < b; i++){
        for(int j = 1; j < b; j++){
            for(int k = 2; k < b; k++){
                if(A[i] * A[i] == A[j] * A[j] + A[k] * A[k]){
                    return 'S';
                }
            }
        }
    }
    return 'N';
}

int main(){
    int A[] = {15, 9, 12, 15, 9, 12};
    char result = RightTriangle(6, A);

    std::cout << result;
    return 0;
}