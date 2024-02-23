#include <iostream>
#include <chrono>
#include <math.h> 

const int N = 1000000000;

// Memory Bound Copy Benchmark
void memoryBoundCopyBenchmark() {
    int* src = new int[N];
    int* dest = new int[N];

    // Start the timer
    auto start = std::chrono::high_resolution_clock::now();

    // Perform the memory copy
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        dest[i] = src[i];
    }

    // Stop the timer
    auto end = std::chrono::high_resolution_clock::now();

    // Calculate the elapsed time
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    std::cout << "Memory Bound Copy Benchmark: " << duration << " milliseconds" << std::endl;

    delete[] src;
    delete[] dest;
}

void computeBoundQuadratureBenchmark() {
    double sum = 0.0;

    // Start the timer
    auto start = std::chrono::high_resolution_clock::now();

    // Perform the quadrature calculation
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < N; i++) {
        double x = double(i) + double(N);
        sum += cos(x);
    }
    // Stop the timer
    auto end = std::chrono::high_resolution_clock::now();

    // Calculate the elapsed time
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    std::cout << "Compute Bound Quadrature Benchmark: " << duration << " milliseconds" << std::endl;
}

int main() {
    memoryBoundCopyBenchmark();
    computeBoundQuadratureBenchmark();

    return 0;
}
