def feb(n):
    if n in [1,2]:
        return 1
    else:
        return feb(n-1)+feb(n-2)
list =[]
for y in range(1,10):
    list.append(feb(y))
print(list)