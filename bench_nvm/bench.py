# coding: utf-8
#
# Codigo com base de teste de benchmark de um codigo Russo.
#
import time

lan=1

if lan==0: 
  import ru
  lang=ru
else :
      import br
      lang=br
a=0
b=0
c=input(lang.cores)
F_1=c
T_1=time.time()
c=c*10000000

while a<c:
  a=a+1
  b=22226545*22+26216*222+88**88*88

T_2=time.time()
t=T_2-T_1
t=c/t
t=t/100000

print lang.res ,lang.ocore ,t

F_2=F_1*4*(t/10)
F_1=F_1*t

print lang.res, lang.ncore, F_1
print lang.flops ,F_2

if t>0 :
      if t<15 : print lang.bed
if t>15 :
      if t<20 : print lang.nbed
if t>20 : 
      if t<25 : print lang.good
if t>25 : print lang.vgood