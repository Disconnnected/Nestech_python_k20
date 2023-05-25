#!/usr/bin/env python3
import random

def solve(N):
    """Creates a list which contains N random integers, each >=0, <=9

    To generate 1 random integer, use::

      import random
      random.randrange(0, 10)

    Must: use list comprehension
    Tips: list comprehension always create new list
    """
    result = None


    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()

import random

#list comprehension
lst = [random.randrange(0,10) for i in range(10)]
#for loop
new_lst = []
for i in range(10):
    new_lst.append(random.randrange(0,10))
print(lst)
print(new_lst)
