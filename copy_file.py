'''
复制文件
'''
filename = input("File:")

try:
     fr = open(filename, 'rb')
except FileNotFoundError as e:
     print(e)
else:
     fw = open('file.jpg','wb')
     while True:
          data = fr.read(1024)
          if not data:
               break
          fw.write(data)
     fr.close()
     fw.close()
