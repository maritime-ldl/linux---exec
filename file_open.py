'''
read函数的用法
fd = open('img.jpg', 'rb')
#fd = open('a.py', 'w')
#print(fd)

data = fd.read()
print(data)
fd.close() 
'''


'''
read实例 
f = open('pore.txt','r')
while True:
     data = f.read(18)
     if not data:
          break
     print(data)
f.close()
'''

'''
readline示例

f = open('pore.txt','r')
while True:
     data = f.readline(8)
     if not data:
          break
     print(data)
f.close()
'''

'''
readlines 示例
f = open('pore.txt','r')
data = f.readlines(18)
print(data)
f.close()
'''
f = open('pore.txt','r')
for i in f:
     print(i)
f.close()


