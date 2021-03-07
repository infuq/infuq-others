# /usr/env/python

'''
迭代器
'''

from collections.abc import Iterator
from collections.abc import Iterable

class Student(Iterable):

    def __init__(self, score):
        self.score = score

    def __iter__(self):
        return MyIterator(self.score)


class MyIterator(Iterator):

    def __init__(self, score):
        self.score = score
        self.index = 0

    def __next__(self):
        try:
            result = self.score[self.index]
        except IndexError:
            # import
            raise StopIteration
        self.index = self.index + 1
        return result        

if __name__ == '__main__':
    
    stu = Student([89, 75, 92, 69])
    for item in stu:
        print(item)

