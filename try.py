"""try:
    age : int(input("please input age\n"))
except:
    print("please input correct age")
"""
"""
def rase_exception():
    age = int(input("please input your age"))
    if age > 120:
        raise Exception("input correct age")

try:
    rase_exception()
except Exception as exp:
    print(exp)
"""
r = 0
while True:
    try:
        r = int(input("plase input thr readis"))
        break
    except:
        print("please input right value")


print(r)