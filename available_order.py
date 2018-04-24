import pymysql.cursors
import aiml
import sys

thisdate = sys.argv[1]

connection = pymysql.connect(host='medicalcenter.martyhumphrey.info',
                             user = 'aardvark9',
                             password = 'sparky12',
                             db = 'Medical',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "SELECT DISTINCT(SlotStart) FROM nurse_sched WHERE SlotDate = %s AND STATUS IS NULL ORDER BY SlotStart;";                    
        cursor.execute(sql, (thisdate, ))
        for row in cursor:
            print(row['SlotStart'])

finally:
    connection.close()
