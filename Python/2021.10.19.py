
from itertools import chain

if __name__ == '__main__':

    arr = [1,2,3]
    dictk = {'k1': 'v1', 'k2':'v2'}

    for v in chain(arr, dictk):
        print(v)