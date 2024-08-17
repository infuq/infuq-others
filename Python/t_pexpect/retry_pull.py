# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
https://blog.csdn.net/qq_45859054/article/details/141280212

pip3 install pexpect
"""

import pexpect
import os
import sys

i = 1
def main():
    global i
    print('invoke main %s' % i)
    i = i + 1

    username = 'infuq'
    password = 'qwert#123'
    
    # 进入到仓库目录
    os.chdir('/mnt/d/Repository/infuq-others')
    
    # 执行拉取
    spawner = pexpect.spawn('git pull')
    try:
        i = spawner.expect(['Username'])
        if i == 0:
            print('input username: ', username)
            # 输入用户名
            spawner.sendline(username)
            i = spawner.expect(['Password'])
            if i == 0:
                print('input password: ', password)
                # 输入密码
                spawner.sendline(password)
                spawner.expect(pexpect.EOF)
                print(spawner.before.decode().strip())
            else:
                # 未出现输入密码的提示, 重试
                main()
        else:
            # 未出现输入用户名的提示, 重试
            main()
    except Exception as e:
        # 出现异常, 重试
        main()

if __name__ == '__main__':
    main()

