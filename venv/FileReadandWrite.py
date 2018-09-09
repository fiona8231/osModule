import os

# f = open(path, 'test.txt')
f = open('test.txt', 'r')

print(f.name)
f.close() # test.txt

print(f.mode) # r

# if we use with the file will automatically closed afterwards

with open('test.txt') as f:
    pass
print(f.closed) #'''True'''

# print contents of file
with open('test.txt') as f:
    f_contents = f.read()
    print(f_contents)

# read the first line of the file
with open('test.txt') as f1:
    f_contents1 = f1.readline()
    print(f_contents1)     

# read content form a extreme large file     

with open('test.txt') as f3:
    for line in f3:
        print(line, end=' ')





