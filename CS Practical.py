x1=1
for i in range(1,6):
    x1=1
    for j in range(1,i+1):
        print(x1, end="     ")
        x1=x1+1
    print()
x2=6
for i in range(6,1,-1):
    x2=6
    for j in range(1,i):
        print(x2, end="     ")
        x2=x2+1
    print()