#include <fstream>
#include <iostream>
#include <cmath>

//compile with g++ 1.5.cpp -std=c++11

// Function to calculate delta_t
double get_delta_t(double delta_x, double buffer) {
    return 0.5 * std::pow(delta_x, 2) * buffer;
}

int main() {
    // Initialization
    int space_steps = 101;
    double delta_x = 1.0 / (space_steps - 1);
    double delta_t = get_delta_t(delta_x, 0.5);
    double time_step_space = 0.3;
    int time_steps = static_cast<int>(std::ceil(time_step_space / delta_t));

    std::vector<double> current_temperature(space_steps, 0.0);
    std::vector<double> next_temperature(space_steps, 0.0);
    std::vector<std::vector<double> > plot_data;

    current_temperature[0] = 350.0;
    current_temperature.back() = 250.0;
    next_temperature[0] = 350.0;
    next_temperature.back() = 250.0;

    // Heat simulation
    for (int i = 0; i < space_steps - 2; ++i) {
        double j = (i + 1) * delta_x;
        current_temperature[i + 1] = 350.0 - 100.0 * j + 200.0 * std::sin(M_PI * j);
    }

    for (int t = 0; t < time_steps; ++t) {
        if (time_step_space - t * delta_t < delta_t) {
            delta_t = time_step_space - t * delta_t;
        }

        for (int j = 0; j < space_steps - 2; ++j) {
            int i = j + 1;
            next_temperature[i] = current_temperature[i] +
                delta_t / std::pow(delta_x, 2) * (current_temperature[i + 1] - 2 * current_temperature[i] + current_temperature[i - 1]);
        }

        current_temperature = next_temperature;
        plot_data.push_back(current_temperature);
    }

    // Write plot data, space_steps, time_step_space, and time_steps to a file
    std::ofstream data_file("plot_data.txt");
    data_file << space_steps << " " << time_step_space << " " << time_steps << "\n";
    for (const std::vector<double>& row : plot_data) {
        for (double value : row) {
            data_file << value << " ";
        }
        data_file << "\n";
    }
    data_file.close();
}