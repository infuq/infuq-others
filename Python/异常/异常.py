#!/usr/bin/env python3


try:
    pass
except:
    print('异常')


try:
    pass
except Exception as e:
    print('捕获所有异常')


try:
    pass
except IOError as e:
    print('捕获指定异常')


try:
    pass
except (IOError, NameError) as e:
    print('捕获多个异常')


try:
    pass
except Exception as e:
    print(e)
else:
    print('在没有异常的时候执行此代码')


try:
    pass
except Exception as e:
    print(e)
else:
    print('在没有异常的时候执行此代码')
finally:
    print('一定会执行此处代码')