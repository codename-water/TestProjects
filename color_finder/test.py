f=open('test.jpg','rb')

newFile=open('newfile.jpg','wb')

for i in f:
    newFile.write(i)