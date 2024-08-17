# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
pip3 install pexpect
"""

import pexpect
import os
import sys

j = 1
def _retry_push():
    global j
    print('invoke retry_push %s' % j)
    j = j + 1

    username = 'infuq'
    password = 'qwert#123'

    spawner = pexpect.spawn('git push')
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
                i = spawner.expect(pexpect.EOF)
                if i == 0:
                    print(spawner.before.decode().strip())
                else:
                    # 重试
                    _retry_push()
            else:
                # 重试
                _retry_push()
        else:
            # 重试
            _retry_push()
    except Exception as e:
        _retry_push()


def main():
    os.chdir('/mnt/d/Repository/infuq-others')
    os.system('git add .')
    os.system('git commit -m "update"')
    _retry_push()


if __name__ == '__main__':
    main()
