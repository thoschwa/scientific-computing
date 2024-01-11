#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <iomanip>

double get_delta_t(double delta_x, double buffer) {
    return 0.5 * std::pow(delta_x, 2) * buffer;
}

int main() {
    // Initialization
    int space_steps = 101;

    double delta_x = 1.0 / (space_steps - 1);
    double delta_t = get_delta_t(delta_x, 0.5);
    double time_step_space = 0.3;

    int time_steps = std::ceil(time_step_space / delta_t);

    std::vector<double> current_temperature(space_steps, 0.0);
    std::vector<double> next_temperature(space_steps, 0.0);
    std::vector<std::vector<double> > plot_data;

    current_temperature[0] = 350.0;
    current_temperature[space_steps - 1] = 250.0;

    next_temperature[0] = 350.0;
    next_temperature[space_steps - 1] = 250.0;

    // Heat simulation
    for (int i = 1; i < space_steps - 1; ++i) {
        double j = i * delta_x;
        current_temperature[i] = 350.0 - 100.0 * j + 200.0 * std::sin(M_PI * j);
    }

    for (int t = 0; t < time_steps; ++t) {
        if (time_step_space - t * delta_t < delta_t) {
            delta_t = time_step_space - t * delta_t;
        }

        for (int j = 1; j < space_steps - 1; ++j) {
            int i = j;
            next_temperature[i] = current_temperature[i] +
                                  delta_t / std::pow(delta_x, 2) * (current_temperature[i + 1] - 2 * current_temperature[i] + current_temperature[i - 1]);
        }

        current_temperature = next_temperature;
        plot_data.push_back(current_temperature);
    }

    // Plotting 3D
    std::ofstream outputFile("output_3D.txt");
    for (int i = 0; i < space_steps; ++i) {
        for (int j = 0; j < time_steps; ++j) {
            outputFile << std::setw(10) << plot_data[j][i];
        }
        outputFile << "\n";
    }
    outputFile.close();

    // Plotting 2D
    std::ofstream outputFile2D("output_2D.txt");
    for (int t = 0; t < time_steps; t += 1000) {
        for (int i = 0; i < space_steps; ++i) {
            outputFile2D << std::setw(10) << current_temperature[i];
        }
        outputFile2D << "\n";
    }
    outputFile2D.close();

    return 0;
}
