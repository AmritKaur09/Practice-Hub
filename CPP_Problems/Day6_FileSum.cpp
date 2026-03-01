#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream file("numbers.txt");  // File to read
    int num, sum = 0;

    if (!file) {
        cout << "Error opening file!" << endl;
        return 1;
    }

    while (file >> num) {
        sum += num;
    }

    file.close();

    cout << "Sum of numbers in file: " << sum << endl;

    return 0;
}