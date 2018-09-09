import os
import shutil

# new a file and copy the images inside the file

oripath = '/Users/Sherry/Desktop/job'
copy_path = '/Users/Sherry/Desktop/job/pic'
#catpth = os.path.join(oripath, 'cat')
#os.mkdir(catpth)
catpth = '/Users/Sherry/Desktop/job/cat'
# what you want to your file name shows like
file_name = ['{}.jpg'.format(i) for i in range(4)]
for file in file_name:
    src = os.path.join(copy_path, file)
    dst = os.path.join(catpth, file)
    shutil.copyfile(src, dst)

# print the number of img in the file
print('Total number of images: ', len(os.listdir(catpth)))
