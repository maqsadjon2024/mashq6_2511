# 5-misol
text = "Python"

for i, ch in enumerate(text, start=1):
    print(f"{i} - {ch}")

# 6-misol
name = "Muhammad"

if len(name) <= 2:
    result = name
else:
    result = name[0] + "X" * (len(name) - 2) + name[-1]

print(result)

# 7-misol
my_tuple = ("a", "b", "c", "d")

result = tuple((i, my_tuple[i]) for i in range(len(my_tuple)))

print(result)

# 8-misol
my_tuple = ("apple", "banana", "ok")

result = tuple(word[::-1] for word in my_tuple)

print(result)
