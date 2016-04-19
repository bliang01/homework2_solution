/*
  example.c

  An example file for directly interacting with your C library. Run `make lib`
  to create the dynamic library. From the top level directory (the directory
  above this one named "homework2-githubusername") run

  $ gcc -Llib -Iinclude -lhomework2 ./ctests/example.c -o example
  $ ./example

*/

#include <stdio.h>
#include "linalg.h"
#include "solvers.h"

int main(int argc, char** argv)
{
  double a[4] = {1, 2, 3, 4};
  double b[4];

  vec_add(b, a, a, 4);  // did you write src/vec_add.c yet?
  for (int i=0; i<4; ++i)
    printf("%f\n", b[i]);
}
