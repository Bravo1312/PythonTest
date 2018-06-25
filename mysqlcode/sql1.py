import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="zq1312", db="testdb")

cursor = db.cursor()
command = "SELECT * FROM test_tb"
cursor.execute(command)
results = cursor.fetchall()
for data in results:
	print(data)

db.close()
