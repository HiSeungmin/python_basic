# Section12_2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/Users/ISIA/python_basic/resource/database.db') # 본인 DB 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone()) # 1번 데이터 읽어오고 다음 위치로 커서 이동

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=0)) # 2번 데이터부터 3개 데이터 읽어오고 다음 위치로 커서 이동

# 전체 로우 선택
# print('All -> \n', c.fetchall())  
# 남은 데이터 즉, 마지막 5번 데이터를 읽어옴. 한 번 더 print하면 데이터 커서가 마지막이라 빈 데이터 읽어옴.

print()

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# 순회2 (순회1을 주석해줘야함. 커서가 마지막을 가리켜서)
# for row in c.fetchall():
#     print('retrieve2 > ', row)

# 순회3 (약간 코드가 복잡해짐)
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve3 > ', row)

print()
