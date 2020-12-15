# 피보나치 수열(Fibonacci Sequence)의 첫 50개 항을 차례대로 출력하는 프로그램을 작성해 보세요.
# 1,1,2,3,5,8,13,21,34,55,...

order = 1
previous = 1
current = 1

while order < 50:
    if order < 2:
        print(current)
        order += 1
        print(current)
        current += 1
        print(f"current : {current}")
        print(f"previous : {previous}")        
    else:
        print(f"---------------")
        order += 1
        print(f"*order : {order}")
        print(f"*previous : {previous}")
        print(current)
        temp = previous
        previous = current
        current = temp + current        


order = 1
previous = 1
current = 1

while order < 50:
    if order < 2:
        order += 1
        current += 1      
    else:
        order += 1
        temp = previous
        previous = current
        current = temp + current