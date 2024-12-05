#include <iostream>
#include <iomanip>
#include <algorithm>

int main() {
    int N, K;
    while(std::cin >> N >> K){

        int a[N];
        for(int i = 0; i < N; i++){
            std::cin >> a[i];
        }
        

        int V = (N * (N - 1) * (N - 2)) / 6;
        float b[V];
        int count = 0;


        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    b[count] = (a[i] + a[j] + a[k]) / 3.0f; 
                    count += 1;
                }
            }
        }


        std::sort(b, b + V);


        std::cout << std::fixed << std::setprecision(1) << b[V-K] << std::endl;

        }
    
    return 0;
}