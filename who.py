import pymysql.cursors
import aiml
import sys
import time
from datetime import date

thistime = sys.argv[1]
thisdate = sys.argv[3]

connection = pymysql.connect(host='medicalcenter.martyhumphrey.info',
                             user = 'aardvark9',
                             password = 'sparky12',
                             db = 'Medical',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        pre_sql = "SELECT COUNT(*) FROM nurse_sched WHERE SlotStart <= %s AND SlotEnd >= %s;"
        cursor.execute(pre_sql, (thistime, thistime, ))
        result = cursor.fetchone()
        if (result['COUNT(*)'] == 0):
            print("The clinic is closed at that time")
        else:
            sql = "SELECT n.FirstName, n.LastName FROM nurses n INNER JOIN nurse_sched s ON n.ID = s.NurseID WHERE s.SlotDate = %s AND s.SlotStart = %s AND s.Status IS NULL;"
            cursor.execute(sql, (thisdate, thistime, ))
            for row in cursor:
                print(row['FirstName'] + " " + row['LastName'])

finally:
    connection.close()

