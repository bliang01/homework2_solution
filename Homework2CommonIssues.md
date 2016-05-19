# How to read the results of grading
You should see in your private repositories
1. `test_homework2_solution.py`: The test suit used to grade the assignments. The performance was tested by timing your `gauss_seidel` code for 4 different problem sizes: 128, 512, 1024 and 2048. More details on this below in the specific issues section.

2. `output.txt`: The raw output when I ran the tests

3. `result.txt`: The parsed test and timing results. I have not used the `jacobi` timings in your performance grades.

You should also see comments in your Canvas grade book for any errors I caught. The points were scaled to the rubric determined for Homework 2.

# Common errors for Homework 2

## General issues:

1. Not initializing arrays. Most students had the declaration part correct. But many of you while using your `linalg.c` functions like `mat_vec` within your `jacobi` and `gauss_seidel` functions would pass it arrays that have not been initialized to 0. Remember that the test suit works with `wrappers.py`, which has `out` initialized to 0. While grading, I have assigned a generous partial credit for everyone who had correct logic and failed the `jacobi` and `gauss_seidel` tests due to this error. But this is a **very dangerous** mistake to make.

2. Inefficient code: `jacobi` and `gauss_seidel` functions for many of you had either
	* Quite a few temporary storage arrays being declared and used. If you can work with the matrix `A` *in place*, you can make the code more efficient and cleaner. Creating `L`, `D` and `U` matrices need `N^2` storage  **each**. These are just copies of `A`’s lower triangular , diagonal and upper triangular sections respectively. *”Better”*: just work with the right elements of `A` itself (refer to solution code). So, always look at your algorithm, *anything* that is either not being changed, or won’t be needed to be preserved, use those matrices *in-place*
	* Many operations that need be done only once, done at each iteration. For example, decomposing the matrix `A` at every iteration, but the only array that changes at every iteration is the guess solution. Decomposing `A` once and reusing the decomposed matrices will help with reducing the computational overhead.
	* Not used your `linalg.c` functions. While this did help some not have initialization errors mentioned above, using functions that have been designed to do all the steps you would need in `jacobi` and `gauss_seidel` algorithms is much more efficient than rewriting the loops from scratch.

## Issues specific to exercises

### For `linalg.c`:
Almost all of you have this correct! The few mistakes I saw were
* Incorrect declarations:
	```c
     double vec_norm(double* v, int N)
     {
    	int norm = 0;
    	for (int i=0; i<N; ++i)
      {
        norm += v[i] * v[i];
      }
    	return norm = sqrt(norm);
	    }```

	 Here `norm` needs to be a `double`, not an integer.

*  Missing initialization:
	```c
     double vec_norm(double* v, int N)
     {
    	double norm;
    	for (int i=0; i<N; ++i)
      {
        norm += v[i] * v[i];
      }
    	return norm = sqrt(norm);
	    }```
   Here `norm` needs to be initialized to `0` before using it.

### For `solve_upper_triangular` or `solve_lower_triangular`:

Very few had these incorrect, missing initialization was the only common issue I observed.

### For `jacobi` and `gauss_seidel`:

Along with the general issues observed above, the most common failed test was:
* Timing tests:  If your code took longer than 60 seconds, the test has failed (I would note that it *timed out*). I computed the std dev range your timing fell in (as per the Grading document rubric). Many of you passed the smaller size problems, most passed the 128 size problem with timings in the -/+ 1 std dev range. But due to efficiency issues noted above, codes would fail at 512 size problems or above. So I weighed the timings for the 128, 512, 1024 and 2048 sizes as 2:1:1:1, so as to maximise partial credit
* If  `test_gauss_seidel` failed, I did not run any timing tests. Unfortunately, I can’t assign any partial performance points (it doesn’t matter how fast you can do something incorrectly). I have made this up by assigning very generous partial credit in the “Passes Tests” grade.
* Some of you copied your working `jacobi` logic/code into `gauss_seidel`. I could not assign any partial credit for the `gauss_seidel` tests and performance tests.
