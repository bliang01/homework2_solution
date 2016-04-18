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
int jacobi(double* out, double* A, double* b, int N, double epsilon)
{
  // create temporary stack storage and initialize `out`
  int num_iter = 0;
  double prev[N];
  double rhs[N];
  for (int i=0; i<N; ++i)
    out[i] = 0;

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
      ++num_iter;
    }

  return num_iter;
}

/*
  Possible performance considerations:
  * copy `out` to stack
  * copy diagonal elements of `A` to stack vector
 */
int gauss_seidel(double* out, double* A, double* b, int N, double epsilon)
{
  // create temporary stack storage and initialize `out`
  int num_iter = 0;
  double prev[N];
  double rhs[N];
  for (int i=0; i<N; ++i)
    out[i] = 0;

  double error = 1;
  while (error > epsilon)
    {
      // update: set prev to out
      //for (int i=0; i<N; ++i)
      //  prev[i] = out[i];

      // compute: rhs = b - L*prev
      //
      // write a custom left-only mat-mul in-place
      for (int i=0; i<N; ++i)
        {
          prev[i] = out[i];
          rhs[i] = 0.0;
          for (int j=0; j<i; ++j)
            rhs[i] += A[i*N + j]*prev[j];
        }
      vec_sub(rhs, b, rhs, N);

      // solve the upper triangular system
      solve_upper_triangular(out, A, rhs, N);

      // compute error: use prev to store (out - prev). we will immediately
      // overwrite it, anyway, at the top of the loop
      vec_sub(prev, out, prev, N);
      error = vec_norm(prev, N);
      ++num_iter;
    }

  return num_iter;
}
