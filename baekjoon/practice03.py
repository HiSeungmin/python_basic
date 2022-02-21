a, b = map(int,input().split())
week = ['MON', 'TUE', 'WED','THU','FRI','SAT','SUN']
d = -1 # week의 인덱스
day = 7
for i in range(1, (a+1)):
    if i==2: # 2월 : 28일까지
        cnt = 0
        for f in range(1,29):
            d += 1
            if(d==7):
                d=0
            cnt+=1
            if a==i and cnt==b:
                day = d

    elif i==4 or i==6 or i==9 or i==11: # 4, 6, 9, 11월 : 30일까지
        cnt =0
        for f in range(1,31):
            d += 1
            if(d==7):
                d=0
            cnt+=1
            if a==i and cnt==b:
                day = d

    else: # 나머지 달 : 31일까지
        cnt = 0
        for f in range(1,32):
            d += 1
            if(d==7):
                d=0
            cnt+=1
            if a==i and cnt==b:
                day = d

print(week[day])
    
