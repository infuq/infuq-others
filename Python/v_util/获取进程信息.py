#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import psutil
import os
import signal

if __name__ == "__main__":

    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        print("pid-%d, pname-%s" % (pid, p.name()))

        # 杀死指定进程
        if p.name() in 'Symantec':
            pass
            os.kill(pid, signal.SIGKILL)
