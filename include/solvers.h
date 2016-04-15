#ifndef __homework2_solver_h
#define __homework2_solver_h

#include "linalg.h"

void solve_lower_triangular(double* out, double* L, double* b, int N);

void solve_upper_triangular(double* out, double* U, double* b, int N);

#endif
