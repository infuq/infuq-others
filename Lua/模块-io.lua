

--[[
    'r' 只读模式
    'w' 创建新文件并写入 或 写入覆盖已有文件内容
    'a' 追加模式
    'r+' 读写模式
    'w+' 
    ‘a+

    '*n' 从当前文件位置读取
    '*a' 从当前文件位置返回文件的所有内容
    '*l' 从当前文件位置读取行, 并将文件位置移动到下一行
    number 读取指定的字节数
]]






-- 写文件
local file = io.open('README.txt', 'w')
file:write('foo.infuq.com')
file:write('\n')
file:close()


-- 读文件
local file = io.open('README.txt', 'r')
local content = file:read("*a")
file:close()
print(content)
