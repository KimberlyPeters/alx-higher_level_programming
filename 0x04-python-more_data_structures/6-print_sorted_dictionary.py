#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_list = list(a_dictionary.keys())
    sort_list.sort()
    for i in sort_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
