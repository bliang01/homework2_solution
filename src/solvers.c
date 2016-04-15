#include "solvers.h"

void solve_lower_triangular(double* out, double* L, double* b, int N)
{
  double temp;
  for (int i=0; i<N; ++i)
    {
      temp = b[i];
      for (int j=0; j<i; ++j)
        temp -= L[i*N + j] * out[j];
      temp /= L[i*N+i];
      out[i] = temp;
    }
}

void solve_upper_triangular(double* out, double* U, double* b, int N)
{
  double temp;
  for (int i=N-1; 0<=i; --i)
    {
      temp = b[i];
      for (int j=N-1; i<j; --j)
        temp -= U[i*N + j] * out[j];
      temp /= U[i*N+i];
      out[i] = temp;
    }
}
