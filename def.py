"""
def print_welcome(name):
    print(name + "Qais ")
    print(name + "Algaralleh ")

print("welcome")
print_welcome("omar ")
print_welcome("karam ")
"""

def clculate_area(r):
    area = r** 2 * 3.14
    return area
r1 = int(input("please input r1\n"))
r2 = int(input("please input r2\n"))
area1 = clculate_area(r1)
area2 = clculate_area(r2)

if area1 > area2:
    print("circle 1 is bigger")
elif area2 > area1:
    print("circle 2 is bigger")
else:
    print("eqwal")
