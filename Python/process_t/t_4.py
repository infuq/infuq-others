#! /usr/bin/env python

'''
pip install psutil
'''

import psutil

if __name__ == '__main__':

    for process in psutil.process_iter():
        # print('{:>5} {:>40} {:<50}'.format(process.pid, process.name(), process.create_time()))

        if process.name() == 'notepad.exe':
            # process.terminate()
            print('找到notepad.exe')







