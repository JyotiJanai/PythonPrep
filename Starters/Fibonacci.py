# Program to display Fibonacci sequence
nterms = int(input("How many numbers?"))

n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Please Enter the Positive Integer")
elif nterms == 1:
    print("Fibocacci Sequence is upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence is:")
    while count < nterms:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count = count + 1
