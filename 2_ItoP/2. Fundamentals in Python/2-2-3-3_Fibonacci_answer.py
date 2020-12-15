order = 1
previous = 0
current = 1

while order <= 50:
    print(current)
    temp = previous
    previous = current
    current = previous + temp
    order += 1