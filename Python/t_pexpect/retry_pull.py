# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
https://blog.csdn.net/qq_45859054/article/details/141280212
pip3 install pexpect
"""

import pexpect
import os
import sys

time = 1
username = 'infuq'
password = 'qwert#123'


def retry():
    global time
    print('invoke retry %s time' % time)
    time = time + 1

    # 进入到仓库目录
    os.chdir('/home/infuq/Repository/infuq-others')

    # 执行拉取
    spawner = pexpect.spawn('git pull', encoding='utf-8')
    spawner.logfile = sys.stdout

    try:
        i = spawner.expect(['Already up to date', 'Username']) # ,timeout = 10

        # 不需要输入用户名和密码的场景
        if i == 0:
            spawner.close()
            return

        # 需要输入用户名和密码的场景
        elif i == 1:
            # 输入用户名
            spawner.sendline(username)
            i = spawner.expect(['Password']) # ,timeout = 10
            if i == 0:
                # 输入密码
                spawner.sendline(password)
                i = spawner.expect(pexpect.EOF)
                if i == 0:
                    spawner.close()

                    status = spawner.status
                    exit_status = spawner.exitstatus
                    signal_status = spawner.signalstatus
                    # 正常退出场景
                    if exit_status == 0:                        
                        return
                    else:
                        # 异常退出场景, 重试
                        retry()
                else:
                    # 异常退出场景, 重试
                    retry()
            else:
                # 未出现输入密码的提示, 重试
                retry()
        else:
            # 未出现输入用户名的提示, 重试
            retry()
    except Exception:
        # 出现异常, 重试
        retry()

if __name__ == '__main__':
    retry()
