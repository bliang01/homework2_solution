#include "linalg.h"
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


/*
  Possible performance considerations:
  * copy `out` to stack
  * copy diagonal elements of `A` to stack vector
 */
void jacobi(double* out, double* A, double* b, int N, double epsilon)
{
  // create temporary stack storage and initialize `out`
  double prev[N];
  double rhs[N];
  //double diag[N];
  for (int i=0; i<N; ++i)
    {
      out[i] = 0;
      //diag[i] = A[i*N + i];
    }


  double error = 1;
  while (error > epsilon)
    {
      // update: set prev to out
      for (int i=0; i<N; ++i)
        prev[i] = out[i];

      // compute: rhs = b - (L+U)*prev
      //
      // compute the equivalent of (L+U)*prev using A by computing A*prev and
      // subtracting the diagonal contribution
      mat_vec(rhs, A, prev, N, N);
      for (int i=0; i<N; ++i)
        rhs[i] -= A[i*N + i] * prev[i];  // *bad access pattern!*
      vec_sub(rhs, b, rhs, N);

      // solve the diagonal system
      for (int i=0; i<N; ++i)
        out[i] = rhs[i]/A[i*N + i];

      // compute error: use prev to store (out - prev). we will immediately
      // overwrite it, anyway, at the top of the loop
      vec_sub(prev, out, prev, N);
      error = vec_norm(prev, N);
    }
}
