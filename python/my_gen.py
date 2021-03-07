# /usr/env/python

def gen():
    yield 1
    yield 2
    yield 3

if __name__ == '__main__':
    
    gen = gen()
    for item in gen:
        print(item)
        
