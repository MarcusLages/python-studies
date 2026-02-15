#include <iostream>

void urlify(std::string &str, const int true_length);

int main() {
    std::string name = "Mrs    Johne Smith          ";
    urlify(name, 18);
    std::cout << "\"" << name << "\"" << std::endl;
}

void urlify(std::string &str, const int true_length) {
    int spaces = 0;
    for(char c: str)
        if(c == ' ')
            spaces++;

    int available_idx = str.length() - 1;
    for(int i = true_length - 1; i >= 0; i--) {
        if(str[i] == ' ') {
            str[available_idx] = '0';
            str[available_idx - 1] = '2';
            str[available_idx - 2] = '%';
            available_idx -= 3;
        } else {
            str[available_idx] = str[i];
            available_idx--;
        }
    }
}