#ifndef __homework2_linalg_h
#define __homework2_linalg_h

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
void vec_add(double*, double*, double*, int);

void vec_sub(double*, double*, double*, int);

double vec_norm(double*, int);

void mat_add(double*, double*, double*, int, int);

void mat_vec(double*, double*, double*, int, int);

#endif
