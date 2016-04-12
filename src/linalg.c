#include "linalg.h"
#include <math.h>

void vec_add(double* out, double* v, double* w, int N)
{
  for (int i=0; i<N; ++i)
    {
      out[i] = v[i] + w[i];
    }
}

void vec_sub(double* out, double* v, double* w, int N)
{
  for (int i=0; i<N; ++i)
    {
      out[i] = v[i] - w[i];
    }
}

double vec_norm(double* v, int N)
{
  double norm = 0.0;
  for (int i=0; i<N; ++i)
    {
      norm += v[i]*v[i];
    }

  return sqrt(norm);
}

void mat_add(double* out, double* A, double* B, int M, int N)
{
  // note that this has good access patterns
  for (int i=0; i<M; ++i)
    {
      for (int j=0; j<M; ++j)
        {
          out[i*N + j] = A[i*N + j] + B[i*N + j];
        }
    }
}

void mat_vec(double* out, double* A, double* x, int M, int N)
{
  // A is (M x N)
  // x is (N x 1)
  for (int i=0; i<M; ++i)
    {
      // perform dot product of row i of A with the vector x
      out[i] = 0.0;
      for (int j=0; j<N; ++j)
        {
          out[i] += A[i*N + j] * x[j];
        }
    }
}

void mat_mat(double* out, double* A, double* B, int M, int N, int K)
{
  // A is (M x N)
  // B is (N x K)
  // out is (M x K) - elt is row A dot col B (over N)
  //
  // naive version for now
  for (int i=0; i<M; ++i)
    {
      for (int j=0; j<K; ++j)
        {
          out[i*M + j] = 0;
          for (int k=0; k<N; ++k)
            {
              out[i*M + j] += A[i*M + k]*B[k*N + j];
            }
        }
    }
}
