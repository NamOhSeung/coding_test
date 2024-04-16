# 이것이 취업을 위한 코딩테스트다 문제

'''
각 자리가 숫자(0~9)로만 이루어진 문자열 S
숫자 사이에 'x' 또한 '+' 연산자 넣어 연산했을 때 가장 큰 수?
단, 모든 연산은 왼쪽에서부터 순서대로 이루어짐. +, x 우선순위 상관 없이 계산함.
'''

num = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(num[0])

for i in range(1, len(num)): # i는 1부터 시작
    number = int(num[i]) # 두번째 인덱스

    if number <= 1 or result <= 1:
        result += number
    else:
        result *= number

print(result)

