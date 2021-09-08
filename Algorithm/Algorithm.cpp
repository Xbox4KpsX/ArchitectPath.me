#include <iostream>
#include <vector>
#include "Search.hpp"
#include "Tree.hpp"

using namespace std;
int main()
{
    // BinarySearch binary;
    deque<int> deq{ 1,2,3,4,5,6 };
    for (auto &i : deq) {
        cout << i << "    ";
        cout << deq.size() << endl;
        deq.pop_front();
    }
}
