#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
pip install psutil
"""

import time
import psutil
import sys
import shutil


def kill_process(killed_process):
    pids = psutil.pids()
    try:
        for pid in pids:
            p = psutil.Process(pid)
            process_name = p.name()
            if process_name in killed_process:
                print("Process name is: %s, pid is: %s" % (process_name, pid))
                try:
                    import subprocess
                    child = subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i" % pid, shell=False)
                    time.sleep(3)
                    child.kill()

                except OSError:
                    if child:
                        child.kill()
                    print('Not found...')
    except:
        pass


def rm_file(files):
    for file in files:
        try:
            shutil.rmtree(file)
        except:
            pass


def all_process():
    for process in psutil.process_iter():
        print('{:>5} {:>40} {:<50}'.format(process.pid, process.name(), process.create_time()))


if __name__ == '__main__':

    while (True):
        
        try:
            kill_process(['time_sched.exe','watch_dog.exe','find_zombie.exe'])
        except:
            pass
        
        try:
            rm_file(["d:/Shell", "d:/t1", "d:/temp"])
        except:
            pass
        
        time.sleep(3)
    # sys.exit(0)


    
