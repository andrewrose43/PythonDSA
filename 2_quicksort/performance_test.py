import timeit

if __name__ == "__main__":
    for v in ["v1", "v2", "v3", "v4"]:
        setup_template = '''
import numpy as np
from {0}.quicksort_{0} import quicksort as {0}'''
        setup = setup_template.format(v)
        code_template = '''
big_list = np.random.randint(0, 99, size=9001)
{0}(big_list)'''
        code = code_template.format(v)
        print("Quicksort " + v + ": {:.5f}".format(timeit.timeit(stmt=code, setup=setup, number=100))+ " seconds")