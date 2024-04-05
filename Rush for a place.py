def fun(ntp):
    n = int(ntp.split()[0])
    t = int(ntp.split()[1]) 
    p = int(ntp.split()[2])
    num = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if p < x and p % t == 0:
                num += 1
            elif p > (x + y - 1) and (p - x - y) % t == 0:
                num = num + 1
    return num
test = int(input(""))
A = []
for i in range(test):
    ntp = input("")
    A.append(ntp)
for i in A:
    print(fun(i))