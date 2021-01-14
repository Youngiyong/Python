import cx_Oracle as oci

print(oci.version)

# 1. 연결객체 얻어오기
oci.connect('scott/tiger@192.168.0.57:1521/orcl')
print('연셜성공')

# 2. 커서객체 얻어오기
# cursor = conn.cursor()
#
# # 3. sql 문장
# sql = "SELECT * FROM emp"
#
# # 4. sql 문장 실행
# cursor.execute(sql)
# cursor.fetchall()
# # 5. 커서객체 닫기
# cursor.close()
# # 6. 커넥션 닫