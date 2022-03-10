#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program calculates the total
#   from user entered numbers


def main():
    # this function shows the total

    # input
    first = int(input("Enter the first number to add (integer): "))
    second = int(input("Enter the second number to add (integer): "))

    # process
    total = first + second

    # output
    print("")
    print("{0} + {1} = {2}".format(first, second, total))

    print("\nDone.")


if __name__ == "__main__":
    main()
