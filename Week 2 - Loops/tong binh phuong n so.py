i  = 1
s = 0
n = input("Nhập n: ")
n = float(n)

while i <= n:
    a = input("Nhập a: ")
    a = float(a)
    s = s + a*a
    i += 1
print (s)