import os

# show the current directory
print(os.getcwd()) #/Users/Sherry/PycharmProjects/starPyrimid

# change directory
os.chdir('/Users/Sherry/Desktop/')

# create folder
os.mkdir('cat')

# create file inside director
os.makedirs('dog/rr')

# remove
os.removedirs('dog/rr')

# rename file/folder
os.rename('cat', 'fish')



# print the files on desktop
print(os.listdir())

# making a new file on Desktop copy.txt
file = open("copy.txt", "w")

# print the text file content in copy.txt
print(os.stat('copy.txt'))

# walk through ALL the directory on Desktop

'''for dirpath, dirname, filename in os.walk('/Users/Sherry/Desktop/'):
    print("current path: ", dirpath)
    print("dir name: ", dirname)
    print("file name: ", filename)
    print()'''

# split file name and extension
print(os.path.splitext('copy.txt')) #('copy', '.txt')
