#include <iostream>
#include <vector>
using namespace std;

/*
A - Unsorted vector
p - Position of first element of vector
r - Position of last element of vector
*/
void merge(std::vector<int> &A, std::vector<int> &L,
           std::vector<int> &R) // MERGE sub-routine
{
  int i = 0, j = 0, k = 0;

  while (i < L.size() && j < R.size()) {
    if (L.at(i) < R.at(j)) {
      A[k] = L.at(i);
      i = i + 1;
    } else {
      A[k] = R.at(j);
      j = j + 1;
    }
    k = k + 1;
  }
  while (i < L.size()) {
    A[k] = L.at(i);
    i = i + 1;
    k = k + 1;
  }

  while (j < R.size()) {
    A[k] = R.at(j);
    j = j + 1;
    k = k + 1;
  }
}

void merge_sort(std::vector<int> &A) {
  if (A.size() <= 1)
    return;
  int q = A.size() / 2;

  std::vector<int> L;
  std::vector<int> R;

  for (int i = 0; i < q; i++)
    L.push_back(A.at(i));

  for (int i = q; i < A.size(); i++)
    R.push_back(A.at(i));

  merge_sort(L);
  merge_sort(R);
  merge(A, L, R);
}

int main() {
  int n;
  std::vector<int> A;
  A.reserve(100);
  cout << "Enter size\n";
  cin >> n;
  cout << "Enter vector\n";
  int input;
  for (int i = 0; i < n; i++) {
    cin >> input;
    A.push_back(input);
  }

  merge_sort(A); // SORT

  for (int i = 0; i < n; i++) // DISPLAY
    cout << A.at(i) << " ";
}