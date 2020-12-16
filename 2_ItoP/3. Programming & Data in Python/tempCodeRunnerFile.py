########## 01. Aliasing ##########
x = [1, 2, 3, 4, 5]
y = x
y[2] = -100
print(x)
print(y)

print('----------------')

x = [-10, -20, -30, -40, -50]
y = list(x)
y[2] = 700
print(x)
print(y)