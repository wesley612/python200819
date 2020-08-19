import os.path
if  os.path.isfile('h.txt'):
    print('存在')
    file = open('h.txt','a')
    file.write('檔案94存在')
    
else:
    print('不存在') 
    file = open('h.txt','a')
    file.write('這是新的檔案')
