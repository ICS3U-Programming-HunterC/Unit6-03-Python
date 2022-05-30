#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 29, 2022
# This program generates 10 random numbers between 1 and 100 and
# displays them to the user and then finds the minuimum value of the numbers

import random


def get_min_value(array_of_num):
    # declare variable
    min_value = 101

    # find the min value
    for a_num in array_of_num:
        if min_value > a_num:
            min_value = a_num

    return min_value


def main():
    # declare constants
    MAX_SIZE = 10
    MAX_NUM = 100
    MIN_NUM = 1

    # create an empty list
    array_of_num = []

    for counter in range(0, MAX_SIZE):
        # generate random number
        random_number = random.randint(MIN_NUM, MAX_NUM)

        # add the number to the list
        array_of_num.append(random_number)

        min_value = get_min_value(array_of_num)
        # print the random number generated and the position it is in the list
        print(
            "{} added to the list at position {}".format(array_of_num[counter], counter)
        )

    # display the minimum value
    print()
    print("The minimum value is: {}".format(min_value))


if __name__ == "__main__":
    main()
