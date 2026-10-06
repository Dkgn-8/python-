#2-1 출력 예측      
for i in range(2,8,2):
    print(i) #2, 4, 6   
    
#2-2 출력 예측
s= 0
for i in range(1,6):
    if i == 3:
        continue
    s += i
print(s)

#2-3 직접 작성: 3의 배수만 출력
for i in range(1,21):
    if i % 3 ==0:
        print(i)
        
#2-4 오류수정
'''
i = 0
while i < 3:
    if i == 1:
        continue
    i +=1
print(i)
'''
i = 0
while i < 3:
    i += 1
    if i == 1:
        continue
print(i)  #증가를 먼저 하고 continue를 만나면 다음 반복으로 넘어가도록 수정