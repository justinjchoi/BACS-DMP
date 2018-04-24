import pymysql.cursors
import aiml
import sys

thisname = sys.argv[1]
thisdate = sys.argv[2] 

connection = pymysql.connect(host='medicalcenter.martyhumphrey.info',
                             user = 'aardvark9',
                             password = 'sparky12',
                             db = 'Medical',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

try:    
    with connection.cursor() as cursor:
        pre_sql = "SELECT COUNT(*) FROM nurses n WHERE n.FirstName = %s"
        cursor.execute(pre_sql, (thisname, ))
        result = cursor.fetchone()
        if result['COUNT(*)'] == 0:
            print("I am not aware of that person")
        else:
            sql = "SELECT s.SlotStart FROM nurses n INNER JOIN nurse_sched s ON n.ID = s.NurseID WHERE n.FirstName = %s AND s.SlotDate = %s AND s.Status IS NULL"
            #sql = "SELECT * FROM nurses WHERE FirstName = %s";
            cursor.execute(sql, (thisname, thisdate, )) 
            for row in cursor:
                print(row['SlotStart'])

finally:
    connection.close()

