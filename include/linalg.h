#ifndef __homework2_linalg_h
#define __homework2_linalg_h

// EXAMPLE FUNCTION DOCS
//
/*
  vec_add

  Computes the sum of two vectors.

  Parameters
  ----------
  out : double*
    The resulting sum vector. (Output by reference.)
  v : double*
  w : double*
    The two vectors to sum.
  N : int
    The length of the vectors, `out`, `v`, and `w`.

  Returns
  -------
  out : double*
    (Output by reference.) The sum of `v` and `w`.
*/
void vec_add(double* out, double* v, double* w, int N);

void vec_sub(double* out, double* v, double* w, int N);

double vec_norm(double* v, int N);

void mat_add(double* out, double* A, double* B, int M, int N);

void mat_vec(double* out, double* A, double* x, int M, int N);

#endif
