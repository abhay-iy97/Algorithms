#include <iostream>
#include <vector>
using namespace std;

void swap(int &x, int &y) {
  int t = x;
  x = y;
  y = t;
}

int partition(int A[], int l, int r) // Partition sub-routine
{
  int pivot = A[r], index = l - 1;

  for (int j = l; j < r; j++) {
    if (A[j] < pivot) {
      index++;
      swap(A[index], A[j]);
    }
  }
  swap(A[index + 1], A[r]);
  return index + 1;
}

void quick_sort(int A[], int l, int r) {
  if (l < r) {
    int p_index = partition(A, l, r);
    quick_sort(A, l, p_index - 1);
    quick_sort(A, p_index + 1, r);
  }
}

int main() {
  int n;
  int A[100];
  cout << "Enter size\n";
  cin >> n;
  cout << "Enter vector\n";
  for (int i = 0; i < n; i++) {
    cin >> A[i];
  }

  quick_sort(A, 0, n - 1); // SORT

  for (int i = 0; i < n; i++) // DISPLAY
    cout << A[i] << " ";
}