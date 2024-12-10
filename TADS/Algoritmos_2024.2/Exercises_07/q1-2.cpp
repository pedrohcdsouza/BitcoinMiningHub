#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

// Aumenta a capacidade do array
int* increase_capacity(int* data, int& capacity, int& size) {
    int* new_array = new int[capacity + 20000];
    for (int i = 0; i < size; ++i)
        new_array[i] = data[i];
    delete[] data;
    capacity += 20000;
    return new_array;
}

// Adiciona um valor ao array
int* push_back(int* data, int& capacity, int& size, int value) {
    if (size == capacity)
        data = increase_capacity(data, capacity, size);
    data[size++] = value;
    return data;
}

int main() {
    std::vector<std::string> arquivosEntrada = {
        "testes\\teste-01.txt", "testes\\teste-02.txt", "testes\\teste-03.txt", "testes\\teste-04.txt",
        "testes\\teste-05.txt", "testes\\teste-06.txt", "testes\\teste-07.txt", "testes\\teste-08.txt",
        "testes\\teste-09.txt", "testes\\teste-10.txt"
    };

    std::ofstream arquivoSaida("resultado-4.txt");
    if (!arquivoSaida.is_open()) {
        std::cerr << "Erro ao abrir arquivo de saída!" << std::endl;
        return 1;
    }

    for (const auto& nomeArquivo : arquivosEntrada) {
        std::ifstream arquivoEntrada(nomeArquivo);
        if (!arquivoEntrada.is_open()) {
            std::cerr << "Erro ao abrir arquivo: " << nomeArquivo << std::endl;
            arquivoSaida << "Erro ao abrir arquivo: " << nomeArquivo << std::endl;
            continue;
        }

        int* data = nullptr;
        int size = 0, capacity = 20000, x;
        data = new int[capacity];

        auto beg = std::chrono::high_resolution_clock::now();
        while (arquivoEntrada >> x) {
            data = push_back(data, capacity, size, x);
        }
        auto end = std::chrono::high_resolution_clock::now();

        // Calcula tempo de processamento
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - beg);

        // Salva o resultado no arquivo de saída
        arquivoSaida << "Arquivo: " << nomeArquivo << "\n";
        arquivoSaida << "Quantidade de números lidos: " << size << "\n";
        arquivoSaida << "Capacidade final do vetor: " << capacity << "\n";
        arquivoSaida << "Tempo de processamento: " << duration.count() << " microseconds(s)\n\n";

        // Libera a memória alocada
        delete[] data;

        // Fecha o arquivo de entrada
        arquivoEntrada.close();
    }

    // Fecha o arquivo de saída
    arquivoSaida.close();
    std::cout << "Processamento concluído. Resultados salvos em 'resultado.txt'." << std::endl;

    return 0;
}
