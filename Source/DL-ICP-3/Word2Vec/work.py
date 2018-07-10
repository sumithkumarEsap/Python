x=1
y=2
my_fibo=[1,2]
inp=int(input('enter the number'))
for i in range(inp-2):
    z=x+y
    x=y
    y=z
    my_fibo.append(z)
print(my_fibo)