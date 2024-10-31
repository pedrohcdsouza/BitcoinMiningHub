#include <iostream>

int main(){

    int arrayN[10] = {10,22,33,4,51,66,74,81,9}; // INPUT
    int x = 0;                            // OUTPUT
    int y = 0;
    
    for (int i = 0; i < 10; i++){
        if(y-arrayN[i] > x){
            x = y-arrayN[i];
        }
        y = arrayN[i];
    }
    std::cout << x;
}