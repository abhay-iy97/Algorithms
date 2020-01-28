#include <iostream>
using namespace std;

void swap(int &a, int &b) {
  int t = a;
  a = b;
  b = t;
}
void selection_sort(int A[100], int n) {
  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      if (A[i] > A[j])
        swap(A[i], A[j]);
    }
    P
  }
}
int main() {

  int n, A[100];
  cout << "Enter size\n";
  cin >> n;
  cout << "Enter array\n";
  for (int i = 0; i < n; i++)
    cin >> A[i];
  selection_sort(A, n);
  for (int i = 0; i < n; i++)
    cout << A[i] << " ";
}