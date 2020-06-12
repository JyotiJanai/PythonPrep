class person():
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
	
	def printname(self):
		print(self.fname, self.lname)


x = person("John", "Musk")
x.printname()


class student(person):
	def __init__(self, fname, lname, year):
		##person.__init__(self,fname,lname)
		super().__init__(fname, lname)
		self.graduationyear = year


x = student("Elon", "Musk", 2020)
x.printname()
# x.print
