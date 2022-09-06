import time
import numpy as np
import top_down.td_v1.merge_sort_td_v1 as tdv1
import top_down.td_v2.merge_sort_td_v2 as tdv2
import top_down.td_v3.merge_sort_td_v3 as tdv3
import top_down.td_v4.merge_sort_td_v4 as tdv4
import top_down.td_v5.merge_sort_td_v5 as tdv5
import top_down.td_v6.merge_sort_td_v6 as tdv6
import top_down.td_v7.merge_sort_td_v7 as tdv7
import bottom_up.bu_v1.merge_sort_bu_v1 as buv1
import bottom_up.bu_v2.merge_sort_bu_v2 as buv2
import bottom_up.bu_v3.merge_sort_bu_v3 as buv3
import bottom_up.bu_v4.merge_sort_bu_v4 as buv4

def time_print(version, count: int, desc: str, task: list):
    start = time.time()
    version.merge_sort(task)
    end = time.time()
    print(desc + " Version " + str(count) + ": " + "{:.5f}".format(end - start) + " seconds")

def iterate_versions(versions: list, desc: str, task: list):
    count = 1
    for version in versions:
        time_print(version, count, desc, task)
        count += 1

if __name__ == "__main__":
    big_list = np.random.randint(0, 99, size=90001)
    iterate_versions([tdv1, tdv2, tdv3, tdv4, tdv5, tdv6, tdv7], "Top-down", big_list)
    iterate_versions([buv1, buv2, buv3, buv4], "Bottom-up", big_list)