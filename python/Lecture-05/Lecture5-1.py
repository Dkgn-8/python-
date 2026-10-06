#파일에서 읽기
infile = open("input.txt","r")
line = infile.readline()
while line !="":
    print(line)
    line=infile.readline()
infile.close()


with open("input.txt","r") as infile:
    line = infile.readline()
    
    while line != "":
        print(line,end="")
        line = infile.readline()
        
#파일에 쓰기
infile = open("output.txt","w")
infile.write("김영희\n")
infile.close()

#파일 닫기
f = open("test.txt","w")
#여기서 여러 가지 작업을 한다
f.close()  #파일을 닫는다

#with open("test.txt","w") as f:
#여기서 여러 가지 작업을 한다
#블록을 빠져나오면 자동으로 파일이 닫쳐진다