#include <iostream>

int main(){

    char can = 'N';
    int a, b, c, d, e, f;
    
    std::cin >> a >> b >> c >> d >> e >> f;

    if(a > c+e){
        can = 'S';
    }
    else if(b > d+f){
        can = 'S';
    }
    

    std::cout << can;


    return 0;
}