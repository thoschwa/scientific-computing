#!/bin/bash

# Compile the program
c++-13 -fopenmp 3.5.cpp -o 3.5 -O3

# Run the program with different numbers of threads
for num_threads in 1 2 4 8 10; do
    echo "Running with $num_threads threads"
    export OMP_NUM_THREADS=$num_threads
    ./3.5
done