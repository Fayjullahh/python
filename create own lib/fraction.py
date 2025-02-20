import math
class Fraction:

    def __init__(self , n, d):
        self.num = n
        self.den = d
        self.simplify()
        
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):
          temp_den = self.den * other.den
          temp_one = int(temp_den/self.den)
          temp_two = int(temp_den/other.den)
          temp_num = (temp_one*self.num+temp_two*other.num)

          return Fraction(temp_num,temp_den)
          

          
    def simplify(self):
        gcd = math.gcd(self.num,self.den)
        self.num //= gcd
        self.den //= gcd
