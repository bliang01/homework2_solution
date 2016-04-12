# Homework #2 - Solution

Directory layout:

* `homework2/` - Python wrapper of C library. (The student need not touch this.)
* `src/` - C library source files
* `Makefile` - Makefile for library (`make lib`) and to execute the tests (`make
  test`). Written such that if the student executes `make test` it should
  compile the library first.
* `test_homework2.py` - Python unitests. Imports the wrappers in
  `homework2/wrapper.py` which calls the corresponding C functions and allows
  use of them.

## Compiling and Testing

Run,

```
$ make lib
$ make test
```

or, alternatively,

```
$ make lib
$ python test_homework2.py
```
