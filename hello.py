import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        common_divisor = math.gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def getNumerator(self):
        return self.numerator
    
    def getDenominator(self):
        return self.denominator
    
    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator
    
    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)
    
    def to_decimal(self):
        return round(self.numerator / self.denominator, 2)
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __floordiv__(self, other):
        result = self.__truediv__(other)
        return Fraction(math.floor(result.numerator), result.denominator)
    
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print(f"Sum: {fraction1 + fraction2}")       
print(f"Difference: {fraction1 - fraction2}") 
print(f"Product: {fraction1 * fraction2}")    
print(f"Quotient: {fraction1 / fraction2}")  
