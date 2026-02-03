#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
std::vector<std::string> act;
void logic(int points) {
    if(points < 17) {
        act.push_back("hit");
    }
    else {
        act.push_back("stand");
    }
}
int main() {
    // Put usage here, such as logic(10);
    for (const std::string& s : act) {
        std::cout << s << " ";
    }
    std::cout << std::endl;
    return 0;
}
