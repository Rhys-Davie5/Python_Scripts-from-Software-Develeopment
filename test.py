array = [1, 8, 15]
gen = (x for in array if array.count(x) > 0)
array = [2,8,22]
print(list(gen))