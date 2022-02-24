import math
from random import randint
from types import coroutine
t1 = open('text.txt', 'r', encoding="utf-8")

s1 = t1.read()
print('s1=', s1)
s2 = ''

size = 4

l = [[['*' for i in range(size)] for x in range(size)] for y in range(math.ceil(len(s1)/16))]
key = [ [0,0,1,0],
        [0,0,0,1],
        [0,1,0,0],
        [1,0,0,0]]
print('l=', l)
print('key=', key)

count = 0
for x in range(len(l)):
    for y in range(size):
        for z in range(size):
            if(count>len(s1)-1):
                break
            l[x][y][z] = s1[count]
            count = count + 1       



for x in range(len(l)):
# 0 градусов
    for y in range(size):
        for z in range(size):
            if(key[y][z]== 1):            
                s2 = s2 + l[x][y][z]

# 90 градусов
    for y in range(size):
        for z in range(size):
            if(key[size-z-1][y]== 1):            
                s2 = s2 + l[x][y][z]

# 180 градусов
    for y in range(size):
        for z in range(size):
            if(key[size-y-1][size-z-1]== 1):            
                s2 = s2 + l[x][y][z]

# 270 градусов
    for y in range(size):
        for z in range(size):
            if(key[z][size-y-1]== 1):            
                s2 = s2 + l[x][y][z]

print('зашифрованное сообщение:',s2)

t2 = open('Encrypt.txt','w', encoding="utf-8")

for s in s2:
  t2.write(s)

t1.close()
t2.close()

t1 = open('Encrypt.txt','r', encoding="utf-8")

s2 = t1.read()

s1 = ''

l = [[['' for i in range(size)] for x in range(size)] for y in range(len(l))]

count = 0

for x in range(len(l)):
# 0 градусов
    for y in range(size):
        for z in range(size):           
            if(key[y][z]== 1) & (len(s2)>count):     
                if s2[count] == '*':
                    l[x][y][z] = ''
                else:
                    l[x][y][z] = s2[count]
                count = count + 1

# 90 градусов
    for y in range(size):
        for z in range(size):
            if(key[size-z-1][y]== 1) & (len(s2)>count):            
                if s2[count] == '*':
                    l[x][y][z] = ''
                else:
                    l[x][y][z] = s2[count]
                count = count + 1

# 180 градусов
    for y in range(size):
        for z in range(size):
            if(key[size-y-1][size-z-1]== 1) & (len(s2)>count):            
                if s2[count] == '*':
                    l[x][y][z] = ''
                else:
                    l[x][y][z] = s2[count]
                count = count + 1

# 270 градусов
    for y in range(size):
        for z in range(size):
            if(key[z][size-y-1]== 1) & (len(s2)>count):            
                if s2[count] == '*':
                    l[x][y][z] = ''
                else:
                    l[x][y][z] = s2[count]
                count = count + 1

t2 = open('Decrypt.txt','w', encoding="utf-8")

for x in range(len(l)):
    for y in range(size):
        for z in range(size):           
            s1 = s1 + l[x][y][z]

print('Расшифрованное сообщение:',s1)

for s in s1:
  t2.write(s)

t1.close()
t2.close()