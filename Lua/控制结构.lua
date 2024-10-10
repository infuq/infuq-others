-- 条件语句
if age < 18 then
    print('未成年')
elseif age < 65 then
    print('成年')
else
    print('老年')
end



-- 循环结构
for i = 1,5 do
    print(i)
end

local count = 0
while count < 3 do
    print(count)
    count = count + 1
end

repeat
    print(count)
until count > 5