import math

s2 = ''

t1 = open('text.txt', 'r', encoding="utf-8")

s1 = t1.read()

#Шифрование методом Гронсфельда
key = '314'

for i in range(len(s1)):
	if ord(s1[i]) < 253:
		s2 = s2 + chr(ord(s1[i])+int(key[i%len(key)]))
	else:
		s2 = s2 + chr(ord(s1[i])+int(key[i%len(key)])-255)



row = 0

column = 3

counter = 0

row = math.ceil(len(s2)/column)

l = [['' for i in range(column)] for x in range(row)]

#Шифрование методом двойной перестановки
for i in range(row):
    for j in range(column):
        if counter+1 > len(s2):
            l[i][j] = ' '
        else:
            l[i][j] = s2[counter]
        counter = counter + 1
print(l)

s2= ''
for i in range(column):
    for j in range(row):
            s2 = s2 + l[j][i]
s2 = s2.strip()
print("Зашифрованная строка:", s2)

t2 = open('Encrypt.txt','w', encoding="utf-8")

for s in s2:
  t2.write(s)

t1.close()
t2.close()

t1 = open('Encrypt.txt','r', encoding="utf-8")

s2 = t1.read()

s1 = ''

counter = 0

l = [['' for i in range(row)] for x in range(column)]

for i in range(column):
    for j in range(row):
        if counter+1 > len(s2):
            l[i][j] = ' '
        else:
            l[i][j] = s2[counter]
        counter = counter + 1

s2 = ''
for i in range(row):
    for j in range(column):
            s2 = s2 + l[j][i]
s2 = s2.strip()

for i in range(len(s2)):
	if ord(s2[i]) < 253:
		s1 = s1 +chr(ord(s2[i])-int(key[i%len(key)]))
	else:
		s1 = s1 +chr(ord(s2[i])-int(key[i%len(key)])+255)
print("Дешифрованная строка:", s1)

t2 = open('Decrypt.txt','w', encoding="utf-8")

for s in s1:
  t2.write(s)

t1.close()
t2.close()

