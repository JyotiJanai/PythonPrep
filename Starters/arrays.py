def my_func():
	car = ["Honda", "BMW", "Nissan"]
	car.append("Toyota")
	car.pop(1)
	car.remove("Honda")
	car.append("volvo")
	car.remove("Toyota")
	for x in car:
		print("My favorite car is", x)


my_func()

fruits = ["Apple", "Banana", "Orange", "Apple", "Mango"]
x = fruits.count("Apple")
print(x)
x = fruits.reverse()
print(fruits)
x = fruits.pop(1)
print(fruits)
x = fruits.remove("Apple")
print(fruits)
