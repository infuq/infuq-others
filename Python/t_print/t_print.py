#!/usr/bin/env python3

def p():
    age = 18
    print('年龄%d' % age)

    num = 332
    print('体重%06d' % num)  # 如果不足6位则前面补0

    weight = 3.9
    print('体重%f' % weight)
    print('体重%.3f' % weight)  # 小数点后显示3位

    name = '派森'
    num = 332
    print('姓名%s 体重%d' % (name, num))
    print(f'姓名{name} 体重{num}')

    print('print结束符默认是\n!', end='\t')


if __name__ == '__main__':
    p()

