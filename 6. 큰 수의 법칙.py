import sys

n, m, k = map(int,sys.stdin.readline().split()) # 배열의 크기 n, 숫자가 더해지는 횟수 m, 연속해서 더해지는 최대 횟수 k

data = list(map(int,sys.stdin.readline().split()))

data.sort() # data를 먼저 정렬해준다.

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1 # 더할 때마다 -1씩 빼기
    if m == 0:
        break
    result += second
    m -= 1

print(result)



# 좀 더 시간복잡도를 고려해서 효율적으로 풀게 되면

n, m, k = map(int,sys.stdin.readline().split()) # 배열의 크기 n, 숫자가 더해지는 횟수 m, 연속해서 더해지는 최대 횟수 k

data = list(map(int,sys.stdin.readline().split()))

data.sort() # data를 먼저 정렬해준다.
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기

print(result)