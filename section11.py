# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    next(reader) # 첫 번째 열 pass 시켜서 출력되지 않음. Header를 skip할 때
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) # iter가 있으면 반복문을 사용할 수 있다는 뜻.
    print()

    for c in reader:
        print(c) # 한 row에 리스트 형식으로 출력됨

# 예제2
with open('./resource/sample2.csv','r') as f:
    reader = csv.reader(f, delimiter='|') # |를 기준으로 잘라서 리스트에 넣겠다
    next(reader) 
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) 
    print()

    for c in reader:
        print(c) 
print()

# 예제3 (Dict 변환)
with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f)

    # for c in reader:
    #     print(c)  # 값이 태그를 달고 출력됨

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('------------')


# 예제4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f:      # newline은 새로운 줄바꿈을 하지 않겠다
    wt = csv.writer(f)

    for v in w:        # 조건문을 사용해야할 때 for문을 사용해주는게 좋음
        wt.writerow(v) # 자동으로 줄바꿈 해줌


# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)  # for문을 쓰지 않고 한 번에 쓰는 방법

print()


# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용(openpyxl, xlrd가 내부적으로 있음, 판다스를 만능으로 사용할 수 있음), 구글에 검색하면 reference가 잘 나와있음
# pip install xrld
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname = '시트명' 또는 숫자, header = 숫자, skiprow = 숫자 
# 시트가 여러 개 있을 때 이름을 지정할 수 있음.(숫자로 가져오는게 좋음.) 
# 몇 번째 행을 header로 가져올지. 
# skiprow는 몇 번째 행을 skip할지
xlsx = pd.read_excel('./resource/sample.xlsx',)

# 상위 데이터 확인
print(xlsx.head())
print()

# 데이터 확인
print(xlsx.tail()) # 끝에 부분을 보겠다


# 데이터 확인
print(xlsx.shape) # 행과 열을 보겠다. 행=20개, 열 =7개가 있다.


# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index = False) # index는 열에 인덱스를 부여할지 말지
xlsx.to_csv('./resource/result.csv', index=False)