import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

# Create students table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_record (
        Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        Subject TEXT NOT NULL,
        Mark INTEGER NOT NULL
    )
''')

# Clear old records (optional for clean testing)
cursor.execute('DELETE FROM student_record')
conn.commit()

# Student data (excluding Enrollment — auto-generated)
student_record = [
    ('ASHUTOSH KUMAR SINGH', 'PWP', 95),
    ('HARSH VISHALBHAI TRIVEDI', 'PWP', 85),
    ('VIRAJ PRAKASHBHAI VAGHASIYA', 'PWP', 90),
    ('SHIVAM ATULKUMAR BHATT', 'PWP', 93),
    ('DEVENDRASINH DOLATSINH JADEJA', 'PWP', 75)
]

# Insert records
cursor.executemany('''
    INSERT INTO student_record (name, Subject, Mark)
    VALUES (?, ?, ?)
''', student_record)

# Commit the changes
conn.commit()

# Fetch and display all records
cursor.execute('SELECT * FROM student_record')
rows = cursor.fetchall()
print("All Student Records:")
for row in rows:
    print(row)
# Fetch student got more than 90
cursor.execute('SELECT name, subject, Mark FROM student_record WHERE Mark > 90')
high_marks = cursor.fetchall()
print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)
# Update MArk for Ashutosh kumar (PWP)
cursor.execute('''UPDATE student_record SET Mark = 98 
                  WHERE name = 'ASHUTOSH KUMAR SINGH' AND subject = 'PWP' ''')

# Commit the changes
conn.commit()
# Verify the update
cursor.execute('SELECT name, MArk FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH"')
updated_mark = cursor.fetchone()
print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}")
# Delete a student record (e.g.,DEVENDRASINH DOLATSINH JADEJA )
cursor.execute('''DELETE FROM student_record WHERE name = 'DEVENDRASINH DOLATSINH JADEJA' ''')

# Commit the changes
conn.commit()

# Verify the deletion
cursor.execute('SELECT * FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
deleted_name = cursor.fetchone()

if deleted_name is None:
    print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")
# Calculate the average Mark
cursor.execute('''SELECT AVG(Mark) FROM student_record''')
avg_mark = cursor.fetchone()[0]

print(f"\nThe average mark of students is: {avg_mark:.2f}")
