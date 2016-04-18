#ifndef __homework2_solver_h
#define __homework2_solver_h

#include "linalg.h"

void solve_lower_triangular(double* out, double* L, double* b, int N);

void solve_upper_triangular(double* out, double* U, double* b, int N);

// jacobi returns the number of iterations by value as an `int`. (it also
// returns the solution vector by reference as `out`)
int jacobi(double* out, double* A, double* b, int N, double epsilon);

// gauss_seidel returns the number of iterations by value as an `int`. (it also
// returns the solution vector by reference as `out`)
int gauss_seidel(double* out, double* A, double* b, int N, double epsilon);

#endif
