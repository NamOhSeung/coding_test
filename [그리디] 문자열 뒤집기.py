# 0010101 => 3
# 0011011 => 2
# 0011000 => 1
# 0011011 => 2

s = input()

count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해 처리
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번재 원소부터 모든 원소를 확인
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        # 다음 수가 1로 바뀌는 경우
        if s[i+1] == '1':
            count0 += 1 # 1이 생겼으니 1을 0으로 바꿔주기 위해 경우가 1이 생긴다.
        else:
            count1 += 1

print(min(count0, count1))
