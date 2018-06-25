import pymysql

db = pymysql.connect("localhost", "root", "zq1312", "testdb")
cursor = db.cursor()

command = "UPDATE test_tb SET score=60 WHERE name='Tom'"

try:
	cursor.execute(command)
	db.commit()
except Exception as e:
	db.rollback()
	print('Error appears!')
finally:
	db.close()	
