"""
tup = (10, 20, 25.5, "Qais", False)
found = False
for t in tup:
    if t == 2.4:
        found = True
        break
    if t == 25.5:
        continue
    print(t)

if found == True:
    print("founded")
else:
    print("not founded")
print("..............")
i = 0
while i <= 5:
    print("Qais")
    i = i + 1
print("*******************")
students = []
i = 0

#while len(students) < 5:
 #   std = input("please input student numbur" + str(i))
  #  i = i + 1
   # students.append(std)


#print(students)

print("*******************")

students = []
while True:
    print("plase input your choice")
    print("1- add student")
    print("2- student")
    print("3- print single student")
    print("4- exit")
    choice = input()
    if choice == "1":
        std = input("please input new student name\n")
        students.append(std)
    elif choice == "2":
        print(students)
    elif choice =="3":
        print("your index rang from 0 to "+str(len(students)))
        index = input("please input student index\n")
        index = int(index)
        print(students[index])


    elif choice == "4":
        break
    else:
        print("invalid input")
        continue
    print("thanks")
print("********************")

print("qais")

print("program start")
mark = input()
mark = int(mark)
if mark >= 50:

    print("yes")
else:

    print("no")
print("program end")

var_1 = True
var_2 = 13
var_3 = 1.5
var_4 = "M"
print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

print("hello, please enter you mark:")
mark = int(input())
if mark > 100  or mark < 0:
    print("invalid")
elif mark >=50:
    print("pass")
else:
    print("fail")

print("thank you")
"""
mark_1 = int(input("please input first numbur\n "))
mark_2 = int(input("please input second mark\n "))
mark_3 = int(input("please input third mahrk\n"))
if mark_1 > 100 or mark_1 < 0:
    print("mark_1 is invalid")
elif mark_2 >100 or mark_2 < 0:
    print("mark_2 is invalid")
elif mark_3 >100 or mark_3 <0:
    print("mark_3 is invalid")
else:
    avg = (mark_1+mark_2+mark_3) / 3.0
    print("you avg=", avg)
    if avg >=90:
        print("A")
    elif avg >=80:
        print("B")
    elif avg >=70:
         print("C")
    elif avg >=60:
        print("D")
    else:
        print("F")