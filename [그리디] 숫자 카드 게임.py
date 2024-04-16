
# min 함수로 풀기
N, M = map(int,input().split())

card = [] # 1차원 배열 만들어놓기

for i in range(N):
    card.append(list(map(int,input().split()))) # 2차원 배열 만들기

min_card = []

for i in range(N):
    min_card.append(min(card[i]))

print(max(min_card))

# 2중 for문으로 풀기
N, M = map(int,input().split())

result = 0

for i in range(N):
    data = list(map(int,input().split()))
    # 현재 줄에서 '가장 작은 수 찾기
    min_value = 10001 # 카드의 숫자 최댓값이 10000이므로 10001을 설정
    for a in data:
        min_value = min(min_value, a) # 10001과 각 행의 최솟값을 비교하여 최소값을 업데이트한다.
    result = max(result, min_value) # result를 갱신하며 각 행의 최솟값 중 최댓값을 찾는다.

print(result)

# 입력값

# 3 3
# 3 1 2 
# 4 1 4 
# 2 2 2 

# 2 4
# 7 3 1 8
# 3 3 3 4
