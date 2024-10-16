#! /usr/bin/env python3.7
# -*- coding: UTF-8 -*-


print(10 / 3) # 3.3333333333333335   除
print(10 // 3) # 3  整除
print(10 % 3) # 1   取余
print(ord('A')) # 65
print(ord('中')) # 20013
print(chr(67))  # C
print('\u4e2d\u6587') # 中文


print('汉字'.encode('UTF-8'))
print('ABC'.encode('ASCII'))
print(b'\xe6\xb1\x89\xe5\xad\x97'.decode('UTF-8'))
print(len('汉字'))
print(len(b'ABC'))
print('Hi,%s, you have $%d.' % ('Tom', 100))
print('rate: %d%%' % 7)
print('Hi,{0},you have {1:.2f}%'.format('Tom', 17.125))


dict = {'name':'Libai','School':'Nanjing','Email':'xxx@gmail.com'}

for key in dict.keys():
	print(key,'=',dict.get(key))
for value in dict.values():
	print(value)	
for key,value in dict.items():
	print(key,'=',value)

for c in 'ABCD':
	print(c)

# enumerate函数可以把一个list变成 索引-元素 对
for i,value in enumerate(['A','B','C']):
	print(i,value)


for key,value in [('A','A1'),('B','B1'),(3,31)]:
	print(key,value)


# break
# continue
# pass

int('123')
list(range(5))
range(5)
range(1,11)
float('12.34')
str(100)
str(12.34)
bool(1)
bool('89')
max(2,3,12,5)
abs(-20)

dict = {'Libai':20,'Dufu':12,'Wangwei':30}
print(dict)
print(dict['Dufu']) # 获取
dict['Dufu'] = 21
print('Libai' in dict) # 判断是否在dict中
print(dict.get('Dufu')) # 获取
print(dict.get('Dufu',-1)) # 获取,如果没有返回-1
print(dict.pop('Dufu')) # 弹出
	

language = set(['Java','C','Python'])
lan = set(['C','C++','Shell'])
print(language & lan) # 交集
print(language | lan) # 并集


language = ['Java','C','C++']
language.sort() # 排序
print(language)

str = 'Java'
s = str.replace('J','K')
print(s)
	
	
def _abs(i):
	if isinstance(i,str):
		raise TypeError('Error')
	if not isinstance(i,(int,float)):
		raise TypeError('Error')	
	if i >= 0:
		return i
	else:
		return -i	




# 可变参数
def info(*args):
	for m in args:
		print(m)


language=['Java','C','C++']
info(*language)
info(*['A','B','C'])
info('D','E','F')


# 关键字参数
def info(name,address,**kw):
	print('name',name)
	print('address',address)
	print('kw',kw)


extra={'Email':'xxx@gmai.com','Phone':18701010101}
info('Libai','Jiangsu',**extra)
info('Libai','Jiangsu',**{'School':'Beijing','Science':'IT'})
info('Libai','Jiangsu',School='Beijing',Science='IT')


# 命名关键字参数(限制关键字参数的名字)
# def info(name,address,*,city,school):
# def info(name,address,*,city='Beijing',school):
# def info(name,address,*args,city,school):
# def info(name,address,*args,city='Beijing',school):


# def info(name,address,email='xxx@gmail.com',*args|*,**kw):
# 必选参数、默认参数、可变参数|命名关键字参数、关键字参数


# 切片
lan = ['A','B','C','D','E','F','G','H','I']
print(lan[0:3])
print(lan[-2:-1])
print(lan[0:8:2])

# 判断一个对象是否可迭代
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance({}, Iterable))
print(isinstance({'name':'Libai'}, Iterable))
print(isinstance(123, Iterable))
	

# 列表生成式
li = [i *i for i in range(1,11)]
print(li)
li = [i * i for i in range(1,11) if i % 2 == 0]
print(li)
li = [m +n for m in 'ABC' for n in '123']
print(li)	
dir = [d for d in os.listdir('../')]
print(dir)

L = ['APPLE','ANDROID']
l = [i[0]+i[1:].lower() for i in L]
print(l)


g = (i * i for i in range(100))
print(next(g))
print(next(g))
for i in g:
	print(i)

it = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(it))


print('''第一行
第二行
第三行''')


