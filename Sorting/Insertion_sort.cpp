#include <iostream>
using namespace std;

void insertion_sort(int A[100], int n) {
  for (int j = 1; j < n; j++) {
    int key = A[j];
    int i = j - 1;
    while (i >= 0 && A[i] > key) {
      A[i + 1] = A[i];
      i = i - 1;
    }
    A[i + 1] = key;
  }
}
int main() {
  int n, A[100];
  cout << "Enter size\n";
  cin >> n;
  cout << "Enter array\n";
  for (int i = 0; i < n; i++)
    cin >> A[i];
  insertion_sort(A, n);
  for (int i = 0; i < n; i++)
    cout << A[i] << " ";
}