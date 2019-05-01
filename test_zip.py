a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]

d = [(1,3),(3,5)]
print(d)

zipped = zip(a,b)
print(*zipped)     # 打包为元组的列表

print(*zip(a,c))              # 元素个数与最短的列表一致
