def gcd(m,n):
   while m%n != 0:
       oldm = m
       oldn = n

       m = oldn
       n = oldm%oldn
   return n

class Fraction:

   def __init__(self,top,bottom):

       self.num = top
       self.den = bottom
   
   def show(self):
       print(self.num,"/",self.den)
       
   def __str__(self):
       return str(self.num)+"/"+str(self.den)
   
   #def __add__(self,otherfraction):
       
       #newnum = self.num*otherfraction.den + self.den*otherfraction.num
       #newden = self.den * otherfraction.den
       #common = gcd(newnum,newden)
       
      # return Fraction(newnum//common,newden//common)
   
   def __eq__(self, otherfraction):
       firstnum = self.num * otherfraction.den
       secondnum = otherfraction.num * self.den
   #def __gt__(self,otherfraction):
   	  ##return firstnum>secondnum


   '''def __sub__(self,otherfraction):
      newnum = self.num - otherfraction.num
      newden = (self.den, otherfraction)'''
   def __mul__(self,otherfraction):
    newnum1=self.num * otherfraction.num
    newnum2= self.den* otherfraction.den
    return  newnum1 * newnum2
   def __truediv__(self,otherfraction):
    newnum1=self.num * otherfraction.num
    newnum2= self.den* otherfraction.den
    return newnum1 / newnum2

      

first_fraction = Fraction(3,5)
second_fraction = Fraction(4,5)

print(first_fraction/second_fraction)


