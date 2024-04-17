# 단순히 동전을 화폐 단위 기준으로 정렬한 뒤에, 화폐 단위가 작은 동전부터 하나씩 확인하면서 target 변수를 업데이트하는 방법으로 최적의 해를 계산할 수 있다.

# 4
# 1 2 3 8

N = int(input())
data = list(map(int,input().split()))
data.sort() # 1 2 3 8

target = 1

for i in data:
    if target < i:
        break
    target += i

print(target)
