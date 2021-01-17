# For Google Meet

# Text File containing NAMES and ROLL number and TIME
file = open('attend.txt')

# CREATING ALL NECESSARY LISTS
all = []
present = []
totalstu = []
count = 0
DictOfElem = {}
full = []
numbers = []
regi = {}


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
for a in range(1, 73, 1):
    totalstu.append(int(a))

absentee = []
for i in totalstu:
    if i not in present:
        absentee.append(i)
absentee.sort()
print("Roll Numbers of Absent Students:\n", absentee)
absentCount = 0
for i in absentee:
    absentCount += 1

for i in present:
    if i in DictOfElem:
        DictOfElem[i] += 1
    else:
        DictOfElem[i] = 1

for l, m in DictOfElem.items():
    if m > 1:
        presentCount -= (m-1)

for i in range(0,count, 2):
    result = ''.join(k for k in all[i] if not k.isdigit())
    result = result.split(':')
    full.append(result[0])

for i in full:
    if i in regi:
        regi[i] += 1
    else:
        regi[i] = 1

for p, m in regi.items():
    if m > 1:
        print(p, "has answered ", m, "times")

print("The number of absent students: ", absentCount)
print("The number of Present students: ", presentCount)