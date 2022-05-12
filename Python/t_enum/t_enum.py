#!/usr/bin/env python3


from enum import Enum


class Month(Enum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12


if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print(name, '\t', member, '\t', member.value)

    print(Month.APR.value)

