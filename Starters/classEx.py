class my_class:
	x = 5


print(my_class)
p1 = my_class()
print(p1.x)


class person:
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender


p2 = person("Trisha", 3, "Female")
print(p2.name, p2.age, p2.gender)

p3 = person("john", 26, "Male")
print(p3.name, p3.age)
print(p2.name)
# print(p2.gender)
