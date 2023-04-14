num = str(input('Digite um número: '))
base = int(input('Digite a base: '))
conv = list()
nnum = list()
cnum = 0
for n in num:
  conv.append(int(n))
conv.reverse()
for i, n in enumerate(conv):
  nnum.append(n * base ** i)
for n in nnum:
  cnum += n
print(cnum)
