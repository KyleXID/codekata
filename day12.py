# Day12.Week3(day2) 문자로 구성된 배열을 input으로 받아, 뒤집어서 return하는 함수입니다.
# python내장 함수 reverse()는 쓰지않고 해결해야합니다.

def reverseString(s) :
    a, b = 0, len(s) - 1

    while a <= b:
        s[a], s[b] = s[b], s[a]
        a += 1
        b -= 1
        
    return s

# def reverseString(s) :
#    return s[::-1]
