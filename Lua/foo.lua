
-- 注释

--[[
被注释内容
]]--

-- 函数
function foo(address,year)
	print(address)
end
foo('成都')

function count( ... )
	-- body
end

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



