def zam (x):
    tmp = x [0]
    x [0] = x[len(x)-1]
    x [len (x)-1] = tmp
A = []
m = int(input("Введите длину массива:"))
for i in range (m):
    A.append(int(input()))
print(A)
zam(A)
print(A)