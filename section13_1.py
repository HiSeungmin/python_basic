# Section13_1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성
# 파일 읽기, 키보드로 입력 받기, 외부 소리 재생, 데이터베이스

import random
import time

words = []   # 영어 단어 리스트(1000개 로드)

n = 1       # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip()) # 양쪽 공백 제거 : strip()

# print(words) # 단어 리스트 확인

a = input("Ready? Press Enter Key!") # Enter Game Start!

# print(a) # string 함수로 들어옴

start = time.time()

while n <= 5:
    random.shuffle(words)    # 알아서 순서를 섞어줌 : shuffle()
    q = random.choice(words) # random으로 하나를 뽑아줌

    print()

    print("*Question # {}".format(n))
    print(q)     # 문제 출력

    x = input()  # 타이핑 입력
    
    print()

    if str(q).strip() == str(x).strip(): # 입력 확인(공백 제거)
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")

    n += 1 # 다음 문제 전환

end = time.time() # End Time
et = end - start  # 총 게임시간
et = format(et, ".3f") # 소수 셋째 자리 출력(시간)

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# 수행 시간 출력
print("게임 시간 : ", et, "초","정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':  # 메인에서만 실행할 수 있게
    pass