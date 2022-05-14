

pattern = re.compile(r'正则')
# re.I 忽略大小写
# re.L
# re.M 多行模式,影响^和$
# re.S 单行模式(使.匹配包括换行在内的所有字符)
# re.U
# re.X


替换字符串中的部分内容 返回新的字符串  不改变原字符串
sub -> <class 'str'>

切割
split -> <class 'list'>
查找到满足条件的所有结果
findall -> <class 'list'>

查找到结果即停止搜索
search -> <class 're.Match'>
匹配
match -> <class 're.Match'>