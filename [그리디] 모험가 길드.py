# 이것이 취업을 위한 코딩테스트다 문제

'''
한 마을에 모험가 N명 있음.
공포도가 X인 모험가는 반드시 X명 이상으로 구성된 모험가 그룹에 참여해야 여행
몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요 없음.
여행 떠날 수 있는 그룹 수의 최댓값은?
'''

N = int(input())
adven = list(map(int,input().split()))

adven.sort() # 1 2 2 2 3

group = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in adven:
    count += 1 
    if count >= i: # 인덱스 첫번째 1과 인덱스 세번째 2만 if문 충족
        group += 1
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(group)


