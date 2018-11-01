'''
#将打开的不同文件赋值给不同的句柄
fh1=open("A:/file1.txt","w")
fh2=open("A:/file2.txt","w")
fh3=open("A:/file3.txt","w")
content1="This is fh1"
content2="This is fh2"
content3="This is fh3"

#向file2.txt中写入
fh1.write(content1)
fh2.write(content2)
fh3.write(content3)
fh1.close()
fh2.close()
fh3.close()

ffhh1=open("A:/file1.txt","r")
print(ffhh1.read())
'''
ffhh2=open("A:/file2.txt","r")
while True:
    line=ffhh2.readline()
    if len(line)==0:
        break
    print(line)
ffhh2.close()
