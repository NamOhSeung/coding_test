# 이것이 취업을 위한 코딩테스트다 문제

N, K = map(int,input().split())

count = 0

while True:
    if N%K == 0: # 나누어 떨어지면
        N = N/K
        count += 1 
        if N == 1:
            break
    else: # 나누어 떨어지지 않는다면
        N = N-1
        count += 1
        if N%K == 0: # 나누어 떨어지면
            N = N/K
            count += 1 
            break

print(count)
