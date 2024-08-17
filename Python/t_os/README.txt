print(os.curdir)
print(os.pardir)

# 重命名
os.rename(old, new)
# 删除
os.remove(file)
# 列出目录下的文件
os.listdir(path)
# 获取当前工作目录
os.getcwd()
# 改变工作目录
os.chdir(newdir)
# 创建多级目录
os.makedirs(r"c:\python\test")
# 创建单个目录
os.mkdir("test")
# 删除多个目录
os.removedirs(r"c:\python\test")  # 若目录为空则删除,向上递归,直到目录不为空则停止删除
# 删除单个空目录
os.rmdir("test")

import shutil
shutil.rmtree("test")  # 递归删除文件夹

os.environ

# 获取文件属性
os.stat(file)
# 修改文件权限与时间戳
os.chmod(file)
# 执行操作系统命令
os.system("dir")
# 启动新进程
os.exec(), os.execvp()
# 在后台执行程序
os.spawnv(mode, file, args)
# 终止当前进程
os.exit(), os._exit()
# 分离文件名
os.path.split(r"c:\python\hello.py") --> ("c:\\python", "hello.py")
# 分离扩展名
os.path.splitext(r"c:\python\hello.py") --> ("c:\\python\\hello", ".py")
os.path.splitext(file)[0]
os.path.splitext(file)[-1]
os.path.splitext(file)[-1][1:]

os.path.abspath(path)

# 获取路径名
os.path.dirname(r"c:/python/hello.py") # "c:\\python"
# 获取文件名
os.path.basename(r"c:/python/hello.py") # "hello.py"
# 判断文件或目录是否存在
os.path.exists(r"c:/python/hello.py") # True
# 判断是否是绝对路径
os.path.isabs(r"./python/") # False
# 判断是否是目录
os.path.isdir(r"c:/python") # True
# 判断是否是文件
os.path.isfile(r"c:/python/hello.py") # True
# 判断是否是链接文件
os.path.islink(r"c:/python/hello.py") # False
# 获取文件大小(字节)
os.path.getsize(filename)
# 搜索目录下的所有文件
os.path.walk()
# 将分离的各部分组合成一个路径名
os.path.join(path1[, path2[, ...]])


os.path.getatime\ctime\mtime
分别返回最近访问、创建、修改时间

print(__file__)
