#include "linalg.h"
#include <math.h>

void vec_add(double* out, double* v, double* w, int N)
{
  for (int i=0; i<N; ++i)
    {
      out[i] = v[i] + w[i];
    }
}
