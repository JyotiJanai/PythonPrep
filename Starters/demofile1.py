f = open("demofile.txt", "r")
# print(f.readline())
# print(f.readline())
# for x in f:
# 	print(x)
# f.close()

f = open("demofile.txt", "a")
f.write("Now I am adding some more content")
f.close()

f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "w")
f.write("Oops I deleted the some content")
f.close()

f = open("demofile.txt", "r")
print(f.read())

f = open("demofile2.txt", "w")
f.write("Hello, I am overwriting this file")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
