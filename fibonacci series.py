#fibonacci series..
num=int(input("enter nTH term of fibonacci series:"))
a, b = 0, 1
for i in range(num+1):
    print(a, end=" ")
    a, b = b, a + b