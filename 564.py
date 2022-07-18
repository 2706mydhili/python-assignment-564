# 1st program for perfect,deficient,abundant
def perfectnum(x):
    addition = 0
    print("proper divisors:")
    for i in range(1,x):
        if(x%i == 0):
         print(i,end=" ")
         addition += i
    print("sum is:",addition)
    return addition
    
x=29
for i in range(1,x):
    summ = perfectnum(i)
    if(summ == i):
       print('%d is a perfect'%i)
    elif(summ < i):
       print('%d is deficient number'%i) 
    else:
       print('%d is abundant'%i)
#6th program
a="Mydhili"
cntc=0
cntl=0
cnt=0
for i in a:
  if(i.isupper()):
    cntc+=1
  elif(i.islower()):
    cntl+=1
  else:
    cnt+=1

print("no of digits : ",cnt)
print("no of lowercase letters : ",cntl)
print("no of upper case letters : ",cntc)
from array import  *
a=array('i',[2,3,4,5])
n=int(input("enter search element : "))
for i in a:
	 if(i==n):
	    print("found")
	    print(a.index(i))
	    break
         else:
	    print("not found")
#9th program
import math
class QuadraticEquation:
 def __init__(self,a,b,c):
  self.__a = a
  self.__b = b
  self.__c = c
 def getA(self):
  return self.__a
 def getB(self):
  return self.__b
 def getC(self):
  return self.__c
 def getDiscriminant(self):
  return (self.__b**2) - (4 * self.__a * self.__c)
 def getRoot1(self):
  if self.getDiscriminant()<0:
   return 0
  else:
   D = self.getDiscriminant()
   B = self.getB()
   return (-B + math.sqrt(D))/(2*self.__a)
 def getRoot2(self):
  if self.getDiscriminant()<0:
   return 0
  else:
   D = self.getDiscriminant()
   B = self.getB()
   return (-B - math.sqrt(D))/(2*self.__a)

#Driver Code
a = int(input("Enter a:\t"))
b = int(input("Enter b:\t"))
c = int(input("Enter c:\t"))
obj = QuadraticEquation(a,b,c)
print("Get a:\t",obj.getA())
print("Get b:\t",obj.getB())
print("Get c:\t",obj.getC())
D = obj.getDiscriminant()
if D > 0:
 print("real and unequal roots")
 print("Root1 :\t",obj.getRoot1())
 print("Root1 :\t",obj.getRoot2())
elif D == 0:
 print("real and equal roots")
 print("Root :\t",obj.getRoot1())
else:
 print("Complex Roots")
