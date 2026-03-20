import mysql.connector


conn = mysql.connector.connect(
    user="Rudra",
    password="Kum@rfamily9",
    host="localhost",
    port=3306,
    database="giet"

)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)

cursor.execute("USE giet")
cursor.execute("select * from students")
for row in cursor:
    print(row)

print("\nStudents with salary between 48000 and 65000:")
cursor.execute("SELECT * FROM students WHERE salary BETWEEN 48000 AND 65000")
for x in cursor:
    print(x)

print("\n Following are the students whose address is not delhi:")
cursor.execute("SELECT * FROM students WHERE address != 'Delhi'")
for c in cursor:
    print(c)

print("\n Following are the students whose designation is not Teacher:")
cursor.execute("SELECT * FROM students WHERE designation != 'Teacher'")
for c in cursor:
    print(c)

print("\n Following are the students whose name is either Aman or Naman:")
cursor.execute("SELECT * FROM students WHERE name='Aman' OR name='Naman'")
for c in cursor:
    print(c)

print("\n Following are the students whose name starts with 'A':")
cursor.execute("SELECT * FROM students WHERE name LIKE 'A%'")
for c in cursor:
    print(c)    

print("\n Following are the students whose have exactly 5 charcaters:")
cursor.execute("SELECT * FROM students WHERE name LIKE '_____'")
for c in cursor:
    print(c)

print("Name starts with r: ")
cursor.execute("SELECT * FROM students WHERE name LIKE 'R%'")
for c in cursor:
    print(c)

print("\nHighest salary: ")
cursor.execute("SELECT * FROM students ORDER BY salary DESC LIMIT 3")
for c in cursor:
    print(c)


print("\nLowest salary: ")
cursor.execute("SELECT * FROM students ORDER BY salary ASC LIMIT 1")
for c in cursor:
    print(c)


print("\n Total male employee:  ")
cursor.execute("SELECT SUM(salary) FROM students WHERE gender='M'")
print(cursor.fetchone())

print("\n Average of the females slary: ")
cursor.execute("SELECT AVG(salary) FROM students WHERE gender='F'")
print(cursor.fetchone())


print("\nCount salary greater than 50000: ")
cursor.execute("SELECT COUNT(*) FROM students WHERE salary > 50000")
print(cursor.fetchone())

print("Count per designation: ")
cursor.execute("SELECT designation, COUNT(*) FROM students GROUP BY designation")
for c in cursor:
    print(c)

print("\n Average salary per gender: ")
cursor.execute("SELECT gender, AVG(salary) FROM students GROUP BY gender")
for c in cursor:
    print(c)

print("\n Total salary per city: ")
cursor.execute("SELECT address, SUM(salary) FROM students GROUP BY address")
for c in cursor:
    print(c)

print("\n Designation salary: ")
cursor.execute("SELECT designation, AVG(salary) FROM students GROUP BY designation HAVING AVG(salary) > 50000")
for c in cursor:
    print(c)

print("\n Cities with more then 1 employee:")
cursor.execute("SELECT address, COUNT(*) FROM students GROUP BY address HAVING COUNT(*) > 1")
for c in cursor:
    print(c)

print("\n Whose salary is greater then average salary: ")
cursor.execute("SELECT * FROM students WHERE salary > (SELECT AVG(salary) FROM students)")
for c in cursor:
    print(c)

print("\n Maximum salary employee: ")
cursor.execute("SELECT * FROM students WHERE salary = (SELECT MAX(salary) FROM students)")
for c in cursor:
    print(c)

print("\n Minimum salary employee: ")
cursor.execute("SELECT * FROM students WHERE salary = (SELECT MIN(salary) FROM students)")
for c in cursor:
    print(c)