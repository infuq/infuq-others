#! /usr/bin/env python

import os
import sys

if __name__ == '__main__':

    argv = sys.argv[1:]
    if not argv:
        raise SyntaxError('长度不符合')
    
    comment = ''
    for item in argv:
        comment += item

    add = 'git add .'
    os.system(add)

    commit = 'git commit -m "{}"'.format(comment)
    os.system(commit)

    push = 'git push'
    print(os.system(push))

