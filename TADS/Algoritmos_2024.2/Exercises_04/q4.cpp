#include <iostream>
#include <chrono>

bool prime(long long n) {
    int qty_divs = 0;
    for (long long d = 1; d <= n; ++d)
        if (n % d == 0)
            qty_divs = qty_divs + 1;
    if (qty_divs == 2)
        return true;
    else
        return false;
}

int main() {
    long long n;
    std::cin >> n;

    // Início do cronômetro
    auto beg = std::chrono::high_resolution_clock::now();
    bool p = prime(n);
    // Fim do cronômetro
    auto end = std::chrono::high_resolution_clock::now();

    if (p) 
        std::cout << n << " is prime" << std::endl;
    else 
        std::cout << n << " is not prime" << std::endl;

    auto dur = end - beg; // Duração do cronômetro
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(dur);
    std::cerr << n << " Processing time: "
              << duration.count() << " microsecond(s)" << std::endl;

    return 0;
}
