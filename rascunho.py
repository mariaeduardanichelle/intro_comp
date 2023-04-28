algarismos = list()
restos = list()
nn = exp = 0
num = str(input('Digite um número: '))
baseatual = int(input('Digite a base atual do número: '))
base = int(input('Digite a base para qual você quer realizar a conversão: '))
if base == 10:
  nn = (int(num, baseatual))
else:
  dec = int(num, baseatual)
  while dec // base != 0:
    a = dec 
    restos.append
#   conv = str(dec)
#   print(conv)
#   for a in conv:
#     algarismos.append(a)
#   algarismos.reverse()
#   print(algarismos)
#   for a in algarismos:
#     a = int(a)
#     nn += a * base ** exp 
# print(nn)

