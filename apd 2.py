#NIM 2009106039+10 = 49
n = int(input("Masukkan NIM anda : "))
r = 1
m = 1
while m <= n+10:
  print(r)
  r += 1
  if r == 10:
    r -= 9
  m += 1 