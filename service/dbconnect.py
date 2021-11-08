import mysql.connector
import time

def connectdb():
    db = mysql.connector.connect(host="localhost", user="root", password="subhashini@98", database="task_tracking_system")
    curzor = db.cursor()
    print("\nDatabase Connected Successfully!!!!!!!!!!")
    time.sleep(2)
    print("\nUSER == root\t\tDATABASE == task_tracking_system\n")
    time.sleep(2)


def showtableval():
    db = mysql.connector.connect(host="localhost", user="root", password="subhashini@98", database = "task_tracking_system")
    curzor = db.cursor()
    y = curzor.execute("select * from task")
    x = curzor.fetchall()
    for i in x:
        print("\nTable values are:\n", i)
        time.sleep(2)
    print("\nNo. of rows are: ")
    time.sleep(2)
    curzor.execute("select Count(*) from task")
    print(curzor.fetchall())


def insert(taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon, modifiedon):
    db = mysql.connector.connect(host="localhost", user="root", password="subhashini@98", database="task_tracking_system")
    curzor = db.cursor()
    command = ("insert into task(taskid,taskname,descript,stats,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon, modifiedon)
    curzor.execute(command, data)
    db.commit()


def search(taskid):
    print("\nsearching.....")
    time.sleep(2)
    db = mysql.connector.connect(host="localhost", user="root", password="subhashini@98", database="task_tracking_system")
    curzor = db.cursor()
    print("\nSearch connected")
    command = "select description from task where taskid=%s" % (1001)
    # data=(taskid)
    curzor.execute(command)
    print(curzor.fetchall())