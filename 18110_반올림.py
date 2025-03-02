
import sys

a=int(sys.stdin.readline())

if a==0:
    print(0)
else:
    c=[]
    for i in range(a):
        b=int(sys.stdin.readline())
        c+=[b]
    c.sort()

    n=round(a*0.15+10**(-7))
    # print(n2)
    for i in range(n):
        c.pop()
        del c[0]
    # print(c)    

    print(round(sum(c)/len(c)+10**(-7)))

    
import sys

# 빠른 입력 처리
input = sys.stdin.read
data = input().split()

# 첫 번째 줄: 난이도 개수
n = int(data[0])

# 예외 처리 (0이면 0 출력)
if n == 0:
    print(0)
    exit()

# 난이도 리스트 정렬
scores = sorted(map(int, data[1:]))  # 리스트 한 번에 입력받고 정렬

# 절사 개수 계산
trim = round(n * 0.15+10**(-7))

# 슬라이싱을 이용한 절사 평균 계산
trimmed_scores = scores[trim:-trim] if trim > 0 else scores
avg_difficulty = round(sum(trimmed_scores) / len(trimmed_scores)+10**(-7))

# 결과 출력
print(avg_difficulty)
