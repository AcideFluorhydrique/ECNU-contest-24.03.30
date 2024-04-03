length = int(input(""))
first = str(input(""))
second = str(input(""))
def function(length, first, second):
    A =[]
    B = []
    for i in first:
        A.append(i)
    for i in second:
        B.append(i)
    Adelete = []
    num = 0
    for i in A:
        if i in B:
            B.remove(i)
        else:
            Adelete.append(i)
            num += 1
    a = ""
    b = ""
    for i in Adelete:
        a += str(i)
    for i in B:
        b += str(i)   
    print(num)
    if num != 0:
        print(a)
        print(b)

function(length,first, second)


