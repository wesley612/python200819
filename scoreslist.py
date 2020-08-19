scores = []
maxscores = 0
minscores = 100
total = 0
maxname=''
minname=''


for i in range(5): 
    n=int(input('成績:'))
    name=int(input('請輸入名字:'))
    scores.append(n)
    if n > maxscores:
        maxscores = n 
        maxname=name
        
    if n < minscores:
         minscores = n 
         minname=name
    total = total + n 
s = total/len(scores) 
print('總分:',total)  
print('平均',s)
print('最高分', maxscores,maxname)
print('最低分', minscores,minname)
      