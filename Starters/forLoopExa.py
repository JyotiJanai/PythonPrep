my_list = ["a", "b", "c", "d", "e", "f"]
for x in my_list:
    print(x)

my_set = {1, 2, 3, 4, 5, 6}
for i in my_set:
    print(i)

my_tuple = ("banana", "apple", "orange")
for j in my_tuple:
    if j == "banana":
        continue
    print(j)


def range_fun(x):
    for i in range(3, x, 2):
        print(i)


range_fun(30)

for y in range(10):
    print(y)
else:
    print("Loop if ended")
