#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

// Function to get delta_t
double get_delta_t(double delta_x, double buffer) {
    return 0.5 * pow(delta_x, 2) * buffer;
}

int main() {
    // Parameters
    const int space_steps = 101;
    const double time_step_space = 0.01;
    
    // Calculate delta_x and delta_t
    double delta_x = 1.0 / (space_steps - 1);
    double delta_t = get_delta_t(delta_x, 0.5);

    int time_steps = static_cast<int>(std::ceil(time_step_space / delta_t));

    // Initialize temperature arrays
    std::vector<std::vector<double>> current_temperature(space_steps, std::vector<double>(space_steps, 0.0));
    std::vector<std::vector<double>> next_temperature(space_steps, std::vector<double>(space_steps, 0.0));

    // Initialize boundaries
    for (int i = 0; i < space_steps; ++i) {
        for (int j = 0; j < space_steps; ++j) {
            current_temperature[i][j] = pow(i, 2) + pow(j, 2);
            next_temperature[i][j] = pow(i, 2) + pow(j, 2);
        }
    }

    // Set boundary conditions
    for (int i = 0; i < space_steps; ++i) {
        current_temperature[0][i] = pow(i, 2);
        current_temperature[1][i] = 1 + pow(i, 2);
        current_temperature[i][0] = pow(i, 2);
        current_temperature[i][1] = 1 + pow(i, 2);

        next_temperature[0][i] = pow(i, 2);
        next_temperature[1][i] = 1 + pow(i, 2);
        next_temperature[i][0] = pow(i, 2);
        next_temperature[i][1] = 1 + pow(i, 2);
    }

    // Normalize the initial temperatures
    double max_temp = current_temperature[space_steps - 1][space_steps - 1];
    for (int i = 0; i < space_steps; ++i) {
        for (int j = 0; j < space_steps; ++j) {
            current_temperature[i][j] /= max_temp;
            next_temperature[i][j] /= max_temp;
        }
    }

    // Variables to store plot data
    std::vector<std::vector<double>> plot_data_beginning = current_temperature;
    std::vector<std::vector<double>> plot_data_half;
    std::vector<std::vector<double>> plot_data_end;

    // Heat simulation
    for (int t = 0; t < time_steps; ++t) {
        for (int i = 1; i < space_steps - 1; ++i) {
            for (int j = 1; j < space_steps - 1; ++j) {
                next_temperature[i][j] = current_temperature[i][j] +
                    (delta_t / pow(delta_x, 2)) * (current_temperature[i + 1][j] - 2 * current_temperature[i][j] + current_temperature[i - 1][j]) +
                    (delta_t / pow(delta_x, 2)) * (current_temperature[i][j + 1] - 2 * current_temperature[i][j] + current_temperature[i][j - 1]);
            }
        }

        current_temperature = next_temperature;

        // Store plot data at different time steps
        if (t == time_steps / 2) {
            plot_data_half = current_temperature;
        }
    }
    plot_data_end = current_temperature;

    // Write plot data to files
    std::ofstream file1("plot_data_beginning.txt");
    file1 << space_steps << " " << time_step_space << " " << time_steps << "\n";
    std::ofstream file2("plot_data_half.txt");
    file2 << space_steps << " " << time_step_space << " " << time_steps << "\n";
    std::ofstream file3("plot_data_end.txt");
    file3 << space_steps << " " << time_step_space << " " << time_steps << "\n";

    for (int i = 0; i < space_steps; ++i) {
        for (int j = 0; j < space_steps; ++j) {
            file1 << plot_data_beginning[i][j] << " ";
            file2 << plot_data_half[i][j] << " ";
            file3 << plot_data_end[i][j] << " ";
        }
        file1 << std::endl;
        file2 << std::endl;
        file3 << std::endl;
    }

    file1.close();
    file2.close();
    file3.close();

    return 0;
}
