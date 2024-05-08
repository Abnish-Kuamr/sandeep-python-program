#se1.py--->main program.. resulting the modules with impoer statement 
import test1 as ts
import greet as g, calendar as c
import calendar
print("val of pi={}".format(ts.pi)) #we are re-using the var pim of some program in other program

g.greetperson("Ramu") #we are re-using the function greetperson() of some program in other program

g.greetperson("Rossum")
g.greetperson("Ritche")
print("----------------------------")
print(c.month(2023,5))


