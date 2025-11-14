# attendance.py

from datetime import datetime
from database import get_connection

def clock_in(emp_id):
    db = get_connection()
    cursor = db.cursor()

    now = datetime.now()
    date_today = now.date()
    time_now = now.strftime("%H:%M:%S")

    # Check if already clocked in
    cursor.execute("SELECT * FROM attendance WHERE emp_id=%s AND date=%s", 
                   (emp_id, date_today))
    result = cursor.fetchone()

    if result:
        print("❌ Already clocked in today.")
    else:
        query = "INSERT INTO attendance (emp_id, date, clock_in) VALUES (%s, %s, %s)"
        cursor.execute(query, (emp_id, date_today, time_now))
        db.commit()
        print("✅ Clock In Successful at", time_now)

    cursor.close()
    db.close()


def clock_out(emp_id):
    db = get_connection()
    cursor = db.cursor()

    now = datetime.now()
    date_today = now.date()
    time_now = now.strftime("%H:%M:%S")

    # Check if clock in exists
    cursor.execute("SELECT attendance_id FROM attendance WHERE emp_id=%s AND date=%s",
                   (emp_id, date_today))
    result = cursor.fetchone()

    if result:
        query = "UPDATE attendance SET clock_out=%s WHERE attendance_id=%s"
        cursor.execute(query, (time_now, result[0]))
        db.commit()
        print("✅ Clock Out Successful at", time_now)
    else:
        print("❌ You didn't clock in today.")

    cursor.close()
    db.close()
