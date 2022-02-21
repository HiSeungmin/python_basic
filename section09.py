# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1
f = open('./resource/review.txt','r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환. 닫아줘야함.
f.close()
print()
print("=======================================================================================")

# 예제2
with open('./resource/review.txt','r') as f: # with문은 close를 생략해도 됨. with문이 끝나면 알아서 반환해줌
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print()
print("=======================================================================================")

# 예제3
with open('./resource/review.txt','r') as f: # 한 라인씩 출력됨, strip()를 해주면 공백을 없애줌
    for c in f:
        print(c.strip())

# 예제4
with open('./resource/review.txt','r') as f:
    content = f.read()
    print(">>", content)
    content = f.read() # 또 읽어보면 빈 내용이 출력 됨 : 한 번 읽어보면 커서가 내용의 끝을 가리켜서
    print(">>", content) # 그 다음의 내용이 없기 때문에 출력이 될 게 없어서 빈 내용으로 출력됨.(내용 없음)

# 예제5
with open('./resource/review.txt','r') as f:
    line = f.readline()
    # print(line) # 첫째줄만 읽어옴. 반복문을 사용해야함.
    while line:
        print(line, end='')
        line = f.readline()

print()
print("=======================================================================================")

# 예제6
with open('./resource/review.txt','r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end='***')


print()
print("=======================================================================================")
print()

# 예제7
score = []
with open('./resource/score.txt','r') as f:
    for line in f:
        score.append(int(line)) # 텍스트 파일에 있는 것은 무조건 문자취급함. 숫자로 형변환 해줘야함.
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일쓰기
# 예제1
with open('./resource/text1.txt','w') as f:
    f.write('Nicegirl!\n')

# 예제2
with open('./resource/text1.txt','a') as f:
    f.write('Goodgirl!/n')

# 예제3
from random import randint
with open('./resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list = ['Kim\n','Park\n','Cho\n']
    f.writelines(list)

# 예제5
with open('./resource/text4.txt','w') as f: 
    print('Test Contests1!', file=f) # 파일에 바로 생성됨.
    print('Test Contests2!', file=f)