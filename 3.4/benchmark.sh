#!/bin/bash

# Compile the program
c++ -Xpreprocessor -fopenmp 3.4.cpp -std=c++11 -o 3.4 -lomp

# Run the program with different numbers of threads
for num_threads in 1 2 4 8; do
    echo "Running with $num_threads threads"
    export OMP_NUM_THREADS=$num_threads
    ./3.4
done