#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> read_input(const string& filename) {
    vector<string> result;
    ifstream input_file(filename);
    string line;

    if (!input_file.is_open()) {
        cout << "Could not open file " << filename << endl;
        return result;
    }

    while (getline(input_file, line)) {
        result.push_back(line);
    }

    return result;
}

int calculate_fuel(int mass) {
    if (mass <= 0) {
        return 0;
    }
    return mass + calculate_fuel((mass / 3) - 2);
}

void day1(const vector<string>& input) {
    int total_fuel = 0;

    for (const auto& line : input) {
        total_fuel += (stoi(line) / 3) - 2;
    }

    cout << "Total fuel: " << total_fuel << endl;
}

void day2(const vector<string>& input) {
    int total_fuel = 0;
    
    for (const auto& line : input) {
        int mass = stoi(line);
        total_fuel += calculate_fuel(mass) - mass;
    }

    cout << "Fuel: " << total_fuel << endl;
}

int main() {
    vector<string> input = read_input("input.txt");

    day1(input);
    day2(input);
    
    return 0;
}
