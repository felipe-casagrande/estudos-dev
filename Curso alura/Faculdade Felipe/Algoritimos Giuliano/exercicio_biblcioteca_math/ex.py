import math
ex1 = math.sqrt(121)
ex2 = math.pow(8,4)
ex3_1 = math.ceil(7.9)  
ex3_2 = math.floor(7.9)
ex4 = math.fabs(-45.67)
ex5 = math.factorial(6)
ex6_1 = math.log(20)
ex6_2 = math.log10(1000)
ex7 =  math.pi *5**2
ex8_1 = math.sin(math.radians(60))
ex8_2 = math.cos(math.radians(60))
ex8_3 = math.tan(math.radians(60))
ex9 = math.hypot(9,12)
#10
def circulo_info(raio):
    area = math.pi * raio**2
    circuferencia = 2*math.pi*raio
    return f' area: {area:.2f}, circunferencia: {circuferencia:.2f}'
ex10 = circulo_info(5)
ex11 = math.degrees(math.asin(0.5))
ex12 = math.trunc(7.987)
ex13 = math.gcd(48,18)
ex14 = math.exp(3)
ex15 = math.radians(90)
ex16 = math.degrees(math.pi/2)
ex17 = math.modf(7.89)[0]
ex18 = math.log2(32)
ex19 = math.log10(100)
ex20 = math.degrees(math.acos(0.5))
ex21 = math.degrees(math.atan(1))
ex22 = math.acosh(1)
ex23 = math.asinh(1)
ex24 = math.atanh(0.8) # nao tem como 1 ou maior q 1
ex25 = math.isinf(1e308*10)
ex26 = math.isnan(math.nan) # sim
print(ex3_1)