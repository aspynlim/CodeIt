def is_palindrome(word):
    return word == word[::-1]  # [start:stop:step]
    # 1번째와 2번째에 아무런 값도 주지 않으면 모든 값을 의미
    # 3번째 증감에서 -1을 처리하면 맨뒤에서 부터 역순으로 하나씩

# 테스트
print(is_palindrome("racecar"))  # True
print(is_palindrome("stars"))    # False
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

