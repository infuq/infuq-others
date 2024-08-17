# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
https://blog.csdn.net/qq_45859054/article/details/141280212
pip3 install pexpect
"""

import pexpect
import os
import sys

j = 1
def main():
    global j
    print('invoke main %s' % j)
    j = j + 1

    username = 'infuq'
    password = 'qwert#123'

    os.chdir('D:\Repository\infuq-zone')
    spawner = pexpect.spawn('git pull', logfile=sys.stdout)
    spawner.logfile = None
    #spawner = pexpect.spawn('git pull')
    try:
        i = spawner.expect(['Username']) # ,timeout = 10
        if i == 0:
            print('input username: ', username)
            spawner.sendline(username)
            i = spawner.expect(['Password']) # ,timeout = 10
            if i == 0:
                # 输入密码
                print('input password: ', password)
                spawner.sendline(password)
                exit_code = spawner.sendline('echo $?')
                print('exit_code', exit_code)
                
                i = spawner.expect(pexpect.EOF)
                if i == 0:
                    print(spawner.before.decode().strip())
                else:
                    # 重试
                    main()
            else:
                # 重试
                main()
        else:
            # 重试
            main()
    except Exception as e:
        main()

if __name__ == '__main__':
    main()
