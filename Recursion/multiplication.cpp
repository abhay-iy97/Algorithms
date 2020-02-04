#include <iostream>
using namespace std;

int multiply(int x, int y) {
  if (x == 0)
    return 0;
  int x1 = x / 2;
  int y1 = y + y;

  int prod = multiply(x1, y1);
  if (x % 2 != 0)
    prod += y;
  return prod;
}
int main() {
  int x, y;
  cout << "Enter numbers\n";
  cin >> x >> y;
  cout << multiply(x, y);
}