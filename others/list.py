# coding=utf-8
# Time    : 2018-04-21
# Author  : Eylaine
# File    : list.py


list = ["error", "warn"]
print(list)

list.append("info")
print("append：", end="")
print(list)

count = list.count("warn")
print("count：", end="")
print(count)

list.extend(["debug", "warnning"])
print("extend：", end="")
print(list)

index = list.index("info")
print("index：", end="")
print(index)

list.insert(list.__sizeof__(), "crital")
print("crital：", end="")
print(list)

list.pop()
print("pop：", end="")
print(list)
a = list.pop(1)
print(a)
print(list)

list.remove("info")
print("remove：", end="")
print(list)

list.reverse()
print("reverse：", end="")
print(list)

list.sort()
print("sort：", end="")
print(list)

b = 1, 2, 3
print(b.__len__())