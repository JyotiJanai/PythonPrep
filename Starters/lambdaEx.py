def my_fun(n):
	return lambda a: a * n


my_doubler = my_fun(10)

print(my_doubler(5))
print(my_doubler(100))
