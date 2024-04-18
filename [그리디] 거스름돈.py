
cash_list = [500,100,50,10]

cash = int(input())

# 거슬러 주는 돈의 최소개수
count = 0

for i in cash_list:
    count += cash//i # 몫만큼 더함
    cash = cash % i
    if cash == 0:
        break

print(count)

'''
입력값
1260
출력값
6
'''
