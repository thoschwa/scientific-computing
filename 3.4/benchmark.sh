#!/bin/bash

# Compile the programs
c++-13 3.4.cpp -o 3.4
c++-13 -fopenmp 3.4_parallel.cpp -o 3.4_parallel

echo "Running serial version"
./3.4

# Run the program with different numbers of threads
for num_threads in 1 2 4 8 10; do
    echo "Running with $num_threads threads"
    export OMP_NUM_THREADS=$num_threads
    ./3.4_parallel
done