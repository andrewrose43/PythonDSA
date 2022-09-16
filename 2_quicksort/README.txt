The four variants of quicksort here test all four combinations of two kinds of loop and two kinds of swap syntax.

While investigating the speed of these components, I learned about the "dis" machine code printing tool, which I'll use for future speed analysis instead of this crude approach.

I also learned about timeit, a more precise alternative to time.time(), and used it in performance_test.py, which I will repeat on future DSA practice.