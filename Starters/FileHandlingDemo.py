f = open("myfile1.txt", "w")
f.write("This is my second text file")
f.close()

f = open("myfile1.txt", "r")
print(f.read())

f = open("myfile12.txt", "w")
f.write("Hello")
f.close()

f = open("myfile12.txt", "r")
print(f.read())
