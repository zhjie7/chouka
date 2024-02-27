"""
180抽大保底，90抽小保底
10抽必出4星
90抽必出5星  抽到的时候up和常驻各占50%
P = {
0.006                       i<=73
0.006 + 0.06(i - 73)        74<=i<=89
1                           i=90
}
五星中奖概率为0.6%
四星角色概率为2.55%
四星武器概率为2.55%
其余的三星概率是96.85%
大保底小报底各占50%
"""
import random

gailv=0
templist=[]

result=[]

pjcjcs=0
pjcjcs2=0

pcount=1

gcount=1

cjcs=0
ljck=0
ljcj=0

upresult=0

count=int()

zika=['三月七','丹恒','虎克','希露瓦','阿兰','娜塔莎','亭云','玲可','佩拉','卢卡','驭空','桑博','素裳','桂乃芬','米沙','雪衣','黑塔','青雀']

up='花火'

changzhu=['克拉拉','瓦尔特','杰帕德','白露','姬子','彦卿','布洛妮娅']

baodi='0'



def start():
   True



def zi():
   zresult=random.choice(zika)
   return zresult

def gold():
   global baodi
   global upresult
   wai=random.choice(['0','1'])
   if (baodi=='1'):
      result=str(up)
      baodi='0' 
      upresult+=1  
   elif (wai=='1'):
      result=random.choice(changzhu)
      baodi='1'
   else:
      result=str(up)
      baodi='0' 
      upresult+=1 
   return result
   
      



def rat():
   if (gcount<74):
      rate=0
   elif(74<=gcount<89):
      rate=gcount-73
   else:
      rate=100
   return rate
    



def chouka():
 for _ in range(count):
  res=random.randint(1, 10000)
  templist.extend([res])
 templist.reverse()
 ckresult()









def ckresult():
   global pcount
   global gcount
   global rate
   global gailv
   global baodi
   global ljcj
   global ljck
   global pjcjcs
   global pjcjcs2
   global cjcs
   for i in range (count):
      ljck+=1
      rate=rat()
      if (templist[i]<=(60+600*rate)):
         result.append(gold())
         pcount+=1
         cjcs=gcount+cjcs
         gcount=1
         gailv=(60+600*rate)/10000
         ljcj+=1
      elif(templist[i]>9490):
         result.append(zi())
         pcount=1
         gcount+=1
      elif(pcount>9):
         result.append(zi())
         pcount=1
         gcount+=1
      else:
         result.extend('-')
         pcount+=1
         gcount+=1
      
         if(upresult>0):
           pjcjcs=cjcs/upresult
         else:
           pjcjcs=0

         if(ljcj>0):
           pjcjcs2=cjcs/ljcj
         else:
           pjcjcs2=0   

   
 
   




          





start()
while True:
    try:
        wish = int(input('1、单抽 2、十连抽 3、重置次数 4、自选次数 5、退出 \n请输入：'))
    except ValueError:
        print('你这输入的啥玩意')
        continue
    if wish == 1:
        count = 1
        chouka()
        print(result,'已垫:'+str(gcount-1),'累计次数:'+str(ljck),'累计出金:'+str(ljcj),'up:'+str(upresult),'累计消耗星琼:'+str(ljck*160),'平均出金抽数:'+(str(pjcjcs2)),'平均up抽数:'+(str(pjcjcs)))
        result=[]
    elif wish == 2:
        count = 10
        chouka()
        print(result,'已垫:'+str(gcount-1),'累计次数:'+str(ljck),'累计出金:'+str(ljcj),'up:'+str(upresult),'累计消耗星琼:'+str(ljck*160),'平均出金抽数:'+(str(pjcjcs2)),'平均up抽数:'+(str(pjcjcs)))
        result=[]
    elif wish == 3:
        result=[]
        gcount=1
        ljck=0
        ljcj=0
        upresult=0
    elif wish == 4:
        count = int(input())
        chouka()
        print('已垫:'+str(gcount-1),'累计次数:'+str(ljck),'累计出金:'+str(ljcj),'up:'+str(upresult),'累计消耗星琼:'+str(ljck*160),'平均出金抽数:'+(str(pjcjcs2)),'平均up抽数:'+(str(pjcjcs)))
        result=[]
    elif wish == 5:
        break
    else:
        print('奇奇怪怪的数字')
        continue











    




 






