#! /usr/bin/env python

# 列表合并4种方法

# 使用 + 号合并列表
score = [1, 3, 5]
books = ['Java', 'C语言精通', True]
ret = score + books
print(ret)

# 2
score.extend(books)  # score内容被修改
print(score)

# 3
score = [1, 3, 5]
score[len(score):len(score)] = books  # 将books内容插入到score最后面
print(score)
score = [1, 3, 5]
score[1:1] = books
print(score)

# 4
level = [1, 3, 5]
books = [True, '深入理解操作系统']
level.append(books)
print(level)
