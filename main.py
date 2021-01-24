# For Google Meet

# Text File containing NAMES and ROLL number and TIME
file = open('attend.txt')

# CREATING ALL NECESSARY LISTS AND DICTIONARIES AND INITIALIZATION OF VALUES

all = []
present = []
totalStudents = []
count = 0
DictOfElem = {}
full = []
numbers = []
register = {}

STUDENTS = int(input("Enter the Total Strength of the class: "))

for line in file:
    count += 1
    line = line.strip()
    all.append(line)

# To get only the roll number of present students by removing their NAMES and the TIME OF RESPONSE
presentCount = 0
for i in range(1, count, 2):
    present.append(int(all[i]))  # Typecasting
    presentCount += 1
present.sort()
print("Roll Numbers of Present Students:\n", present)

# To get the roll numbers of all students
for a in range(1, STUDENTS+1):
    totalStudents.append(int(a))

# appending all absent roll numbers by removing present ones from totalstudents[]
absentee = []
for i in totalStudents:
    if i not in present:
        absentee.append(i)
absentee.sort()
print("Roll Numbers of Absent Students:\n", absentee)
absentCount = 0
for i in absentee:
    absentCount += 1

# To see how many times a roll number has been repeated.
for i in present:
    if i in DictOfElem:
        DictOfElem[i] += 1
    else:
        DictOfElem[i] = 1

# If anyone has answered multiple times, the present students number mustn't increase.
for l, m in DictOfElem.items():
    if m > 1:
        presentCount -= (m-1)

# To get the names of the Students by removing the TIME Element eg-> Akshay Munot10:47 AM = Akshay Munot
for i in range(0, count, 2):
    result = ''.join(k for k in all[i] if not k.isdigit())
    result = result.split(':')
    full.append(result[0])

# To see how many times a student has answered, which will proxy proof the record.
for i in full:
    if i in register:
        register[i] += 1
    else:
        register[i] = 1

for p, m in register.items():
    if m > 1:
        print(p, "has answered ", m, "times")

print("The number of absent students: ", absentCount)
print("The number of Present students: ", presentCount)
