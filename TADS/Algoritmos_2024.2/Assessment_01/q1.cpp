#include <iostream>

int soma(int a, int b) {

int r = a + b;

return r;

}

int main() {

int a, b;
std::cin >> a >> b;
int s = soma(a, b);
std::cout << s << std::endl;

return 0;

}