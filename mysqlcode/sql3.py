#coding=utf-8

import pymysql

db = pymysql.connect("localhost", "root", "zq1312", "testdb")
cursor = db.cursor()

command = ['''
INSERT INTO test_tb
(name, score, sub_date)
VALUES
('Johnasen', 66, NOW())
''',
'''
DELETE FROM test_tb WHERE name='Miki'
''']


try:
	cursor.execute(command[1])
	db.commit()
except:
	db.rollback()
	print("Error Appears!")
finally:
	db.close()
