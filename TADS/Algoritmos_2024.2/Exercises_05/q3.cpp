#include <iostream>

int main(){

    int arrayN[11] = {7,17,9,1,2,1,5,11,31,1,5}; // INPUT
    int x = 0;                                   // OUTPUT
    int y = 0;
    
    for (int i = 0; i < 11; i++){
        if(y-arrayN[i] > x){
            x = y-arrayN[i];
        }
        y = arrayN[i];
    }
    std::cout << x;
}