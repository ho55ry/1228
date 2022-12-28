# -----------------------------------------------------------------------------------------------
# 계산기 프로그램 클래스기반으로 만들기
# 입력, 더하기, 빼기, 곱하기, 나누기
# -----------------------------------------------------------------------------------------------
class Calc:
    def __init__(self):
        self.result=0
    def __add__(self,num):
        self.result += num
        if self.result==int(self.result): return int(self.result)
        else: return self.result
    def __sub__(self,num):
        self.result -= num
        if self.result==int(self.result): return int(self.result)
        else: return self.result
    def __mul__(self,num):
        self.result *= num
        if self.result==int(self.result): return int(self.result)
        else: return self.result
    def __div__(self,num):
        self.result /= num
        if self.result==int(self.result): return int(self.result)
        else: return self.result
ex=Calc()
print(ex.__add__(5))
print(ex.__add__(5.0))
print(ex.__sub__(4))
print(ex.__mul__(2))
print(ex.__div__(5))
print(ex.__div__(2.4))
print(ex.__sub__(1))

# -----------------------------------------------------------------------------------------------
# 2.함수 구현
# 2-1 구구단 2~9단 출력 반복문 1개
# -----------------------------------------------------------------------------------------------
def 구구단(start,end):
    dan=start; num=1; switch=True
    while num != 10:
        if switch:
            print(f'--[{dan}단]--',end='\t')
            dan=dan+1
            if dan==end+1: switch=False; dan=start; print()
        if not switch:
            print(f"{dan}*{num}= {dan*num}",end='\t\t')
            dan=dan+1
            if dan==end+1: dan=start; num=num+1; print()

구구단(2,9)
# -----------------------------------------------------------------------------------------------
# 2-2 구구단 리스트 컴프리헨션
# -----------------------------------------------------------------------------------------------
[]
# -----------------------------------------------------------------------------------------------
# 2-3 별자리, 띠
# -----------------------------------------------------------------------------------------------
id=input('주민번호 입력(000000-0000000): ')
A=[]
if int(id[7])==1 or int(id[7])==2:
    A.append(19)
else:
    A.append(20)
for i in id:
    if i.isdigit():
        A.append(int(i))
#나이
B=A[0]*100+A[1]*10+A[2]
print(f'{2022-B+1}세',end=', ')
#성별
if A[7]==1 or A[7]==3:print('남자',end=', ')
else: print('여자',end=', ')
#생년월일
print(f'{B}년{A[3]*10+A[4]}월{A[5]*10+A[6]}일',end=' ')
#띠
띠=['원숭이띠','닭띠','개띠','돼지띠','쥐띠','소띠','호랑이띠','토끼띠','용띠','뱀띠','말띠','양띠']
if B%12 ==0: print(띠[0],end=' ')
if B%12 ==1: print(띠[1],end=' ')
if B%12 ==2: print(띠[2],end=' ')
if B%12 ==3: print(띠[3],end=' ')
if B%12 ==4: print(띠[4],end=' ')
if B%12 ==5: print(띠[5],end=' ')
if B%12 ==6: print(띠[6],end=' ')
if B%12 ==7: print(띠[7],end=' ')
if B%12 ==8: print(띠[8],end=' ')
if B%12 ==9: print(띠[9],end=' ')
if B%12 ==10: print(띠[10],end=' ')
if B%12 ==11: print(띠[11],end=' ')
#별자리
C=A[3]*1000+A[4]*100+A[5]*10+A[6]
별자리=['물병자리','물고기자리','양자리','황소자리','쌍둥이자리','게자리','사자자리','처녀자리','천칭자리','전갈자리','궁수자리','염소자리']
if 120 <= C <=218: print(별자리[0])
if 219 <= C <=320: print(별자리[1])
if 321 <= C <=419: print(별자리[2])
if 420 <= C <=520: print(별자리[3])
if 521 <= C <=621: print(별자리[4])
if 622 <= C <=722: print(별자리[5])
if 723 <= C <=822: print(별자리[6])
if 823 <= C <=923: print(별자리[7])
if 924 <= C <=1022: print(별자리[8])
if 1023 <= C <=1122: print(별자리[9])
if 1123 <= C <=1224: print(별자리[10])
if 1225 <= C or C <=119: print(별자리[11])