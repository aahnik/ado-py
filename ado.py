#!/usr/bin/env python

# MIT License
# Copyright (c) 2021 Aahnik Daw

"""
Do stuff with Python

-> write a file do.py

-> write functions in it

-> call any function by running `ado func` in the terminal

-> running only `ado` would print the docstring of do.py
"""


import os
import sys


def import_do():
    sys.path.append(os.getcwd())
    try:
        import do

        return do
    except ImportError as err:
        print(__doc__)
        print(err)
        sys.exit(1)


def main():
    do = import_do()
    if len(sys.argv) == 1:
        print(do.__doc__)
        sys.exit(1)

    todo = sys.argv[1]

    try:
        val = getattr(do, todo)()
        if val:
            print(val)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
