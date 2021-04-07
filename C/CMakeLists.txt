cmake_minimum_required(VERSION 3.15)
project(C C)

set(CMAKE_C_STANDARD 99)

add_executable(C main.c C/_array.c C/_array.h C/_other.h C/_other.c C/_enum.h C/_enum.c C/_union.h C/_union.c C/_struct_1.c C/_struct_2.c C/_struct.h C/_struct_3.c C/_struct_4.c C/_struct_align_1.c C/_struct_align_2.c)