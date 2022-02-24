import math

t1 = open('text.txt', 'r', encoding="utf-8")

s1 = t1.read()

s2 = ''

row = 0

column = 5

counter = 0

row = math.ceil(len(s1)/column)

l = [['' for i in range(column)] for x in range(row)]


for i in range(row):
    for j in range(column):
        if counter+1 > len(s1):
            l[i][j] = ' '
        else:
            l[i][j] = s1[counter]
        counter = counter + 1

for i in range(column):
    for j in range(row):
            s2 = s2 + l[j][i]
s2 = s2.strip()

t2 = open('Encrypt.txt','w', encoding="utf-8")

for s in s2:
  t2.write(s)

t1.close()
t2.close()

print('Зашифрованное сообщение:',s2)

counter = 0

t1 = open('Encrypt.txt','r', encoding="utf-8")

s2 = t1.read()

s1 = ''

l = [['' for i in range(row)] for x in range(column)]

for i in range(column):
    for j in range(row):
        if counter+1 > len(s2):
            l[i][j] = ' '
        else:
            l[i][j] = s2[counter]
        counter = counter + 1

for i in range(row):
    for j in range(column):
            s1 = s1 + l[j][i]
s1 = s1.strip()

print('Дешифрованное сообщение:',s1)

t2 = open('Decrypt.txt','w', encoding="utf-8")

for s in s1:
  t2.write(s)

t1.close()
t2.close()