#include <iostream>
#include <list>
#include <algorithm>

int main(){

    int a[6] = {2,6,4,3,10,1};
    int K = (6 * (6-1)*(6-2)/6);
    int b[K];
    int count = 0;

    for (int i = 0; i < 6; i++){
        for(int j = i + 1; j < 6; j++){
            for(int k = j + 1; k < 6; k++){
                b[count] = (a[i] + a[j] + a[k])/3;
                count += 1;
            }
        }
    }
    

    std::sort(b, b + 20);
    for (int l = 0; l < K; l++){
        std::cout << "indice " << l << " : " << b[l] << "\n";
    }

    std::cout << b[19];

    return 0;
}