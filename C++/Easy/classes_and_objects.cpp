#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

// Write your Student class here
class Student {
    private:
        int s1;
        int s2;
        int s3;
        int s4;
        int s5;
    public:
        void input(){
        cin >> s1 >> s2 >> s3 >> s4 >> s5;
        }
        int calculateTotalScore() {
            return s1 + s2 + s3 + s4 + s5;
        }
};

int main() {
