n = int(input(""))
A = []
for i in range(n):
    line = input("")
    L = []
    for j in line:
        L.append(j)
    A.append(L)
num = 0
for i in range(1, n//2 + 1):
    for j in range(n - 2 * i):
        for k in range(n - i):
            T = True
            for p in range(k, k + i + 1):
                if A[j][p] == "o":
                    T = False
                    break
            for p in range(k, k + i + 1):
                if A[j + i][p] == "o":
                    T = False
                    break
            for p in range(k, k + i + 1):
                if A[j + 2 * i][p] == "o":
                    T = False
                    break
            for p in range(j, j + i + 1):
                if A[p][k] == "o":
                    T = False
                    break
            for p in range(j, j + i + 1):
                if A[p + i][k + i] == "o":
                    T = False
                    break
            if T:
                num += 1
print(num)             
