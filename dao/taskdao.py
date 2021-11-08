import time

from service import dbconnect


def run():
    print("\n<<<<<<<<<<<<\tWELCOME TO TASK TRACKING SYSTEM\t\t>>>>>>>>>>>>")
    time.sleep(2)
    print("\nconnecting to Database........... ")
    time.sleep(2)

    dbconnect.connectdb()
    print("\nInserting the values.....")
    time.sleep(2)
    print("\nData inserted Successfully......")
    time.sleep(2)
    dbconnect.showtableval()
    print("\nCommit successful....")
    time.sleep(2)
