
-- 注释

--[[
被注释内容
]]--

-- 函数
function foo(address,year)
	print(address)
end
foo('成都')

-- 可变参数
function average(...)
    sum = 0
    local avg = {...}
    for i,v in ipairs(avg) do
        sum = sum + v
    end
    return sum / #avg -- #arg表示传入参数的个数
end
print(average(1,2,3))


sum = function(x,y)
	return x + y;
end
print(sum(10,3))



-- 表 类似于哈希
book = {
    name = 'Lua入门',
    price = 35.8,
    year = 2021
}
for k,v in pairs(book) do
    print(k,v)
end
-- 新增属性
book.country = 'China'
book['address'] = '成都'
-- 删除属性
book.price = nil
book['year'] = nil

-- 表 类似于数组
book = {'Lua入门第二版',37.9,2022}
for index,v in pairs(book) do
    print(index,v)
end
-- 新增属性
book[5] = 'China'
-- 删除属性
book[1] = nil


-- 运算符

i = 3
j = 5
print(i and j) -- 如果i为真, 则返回j ; 如果i为假, 则返回i
print(i or j) -- 如果i为真, 则返回i ; 如果i为假, 则返回j




-- 流程控制

-- while
i = 0
sum = 0
while i < 100 do
	i = i + 1
	sum = sum + i
end
print(sum)

-- for
sum = 0
for i=1,100 do
	sum = sum + i
end
print(sum)


-- repeat
i = 100
repeat
	i = i - 1
	sum = sum + 1
until i < 0
print(sum)



-- if 
if sum < 100 then
    print('< 100')
elseif sum < 200 then
    print('< 200')
else
    print('> 200')
end




