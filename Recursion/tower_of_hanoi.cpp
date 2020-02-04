#include <iostream>

void toh(int n, char src, char dst, char tmp) {
  if (n == 1) {
    std::cout << "Move disk " << n << " from " << src << " to " << dst << "\n";
    return;
  }
  toh(n - 1, src, tmp, dst);
  std::cout << "Move disk " << n << " from " << src << " to " << dst << "\n";
  toh(n - 1, tmp, dst, src);
}
int main() { toh(3, 'A', 'C', 'B'); }