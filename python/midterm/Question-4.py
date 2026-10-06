#4-1
a = [10,20,30,40]
print(a[-1])
print(a[1:3])
print(a[:2])

#4-2
a=[1,2]
a.append([3,4])  #한 원소 추가
print(a) # [1,2,[3,4]] 
print(len(a)) # 3
a.extend([3,4])  #원소 여러 개 추가
print(a) # [1,2,[3,4],3,4]

#4-3 직접 작성: 컴프리헨션
print([n for n in range(1,11) if n%2==0])

#4-4
g = [[0]*2]*2
g[0][0] = 9
print(g) # [[9,0],[9,0]] 2차원 리스트를 만들 때는 주의해야 한다. g = [[0]*2 for _ in range(2)]로 해야 한다.
g = [[0]*2 for _ in range(2)]
g[0][0] = 9
print(g) # [[9,0],[0,0]]