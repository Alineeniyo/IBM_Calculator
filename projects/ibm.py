 # Start IBM project
#  Building project in python as first one
from unittest import result
name1 = "Aline"
height_m1= 2
weight_kg1 = 90

name2 = "Kevine"
height_m2 = 1.8
weight_kg2 = 70

name3 ="Assia"
height_m3= 1.8
weight_kg3 = 70

def bmi_cal(name, height_m, weight_kg):
    bmi = weight_kg/(height_m **2)
    print (f"You have {bmi}")
    if bmi<25 :
       return name + " is not over weight"
    else:
       return name + "  is over weight"

result1=bmi_cal(name1, height_m1, weight_kg1)
result2=bmi_cal(name2, height_m2, weight_kg2)
result3=bmi_cal(name3, height_m3, weight_kg3)
print(result1)
print(result2)
print(result3)

