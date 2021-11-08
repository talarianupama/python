from dao import taskdao
import dbconnect

taskid=1001
taskname='add'
description='anu is added'
status='completed'
priority=1
notes='notes 1'
bookmark='book_mark 01'
ownerid=111
creatorid=1
createdon='2021-10-03'
modifiedon='2021-10-14'


taskdao.run()
dbconnect.search(1001)
