#include <stdio.h>
#include <string.h>

void logic(int money, int points) {
    char act[10] = ""; 
    double bet = 0.0;

    if (money >= 99) {
        if (points >= 17) {
            strcpy(act, "stand");
        } else {
            strcpy(act, "hit");
            bet = money * 0.25;
        }
    } else {
        if (points > 16) {
            strcpy(act, "stand");
        } else {
            strcpy(act, "hit");
            bet = money * 0.1;
        }
    }
    if (strlen(act) == 0) {
        strcpy(act, "stand");
    }
}
int main() {
    // Usage: logic(money, points);
    return 0;
}
