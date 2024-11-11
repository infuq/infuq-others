local l = {'Java','Python','C++'}
print(l)
print(l[1])
-- 如果 table 是数组,那么它的长度就是数组中元素的个数
print(#l)
-- 遍历
for index,value in ipairs(l) do
    print(index,value)
end



local t = {
    i = 3,
    j = 5,
    k = 7
}
print(t)
print(t['j'])
-- 如果 table 是map,那么它的长度就是map中key的个数
print(#t)
-- 遍历
for key,value in pairs(t) do
    print(key, value)
end
