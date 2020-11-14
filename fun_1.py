name= input("enter your name \n")
weight = float(input("enter your weight in kg\n"))
height = float(input("enter your height in m\n"))

def bmi_calculation(name,weight,height):
    bmi=weight/(height**2)
    print("bmi",bmi)
    if(bmi<=25):
        return name + " not overweight"
    else:
        return name +" overweight"

a= bmi_calculation(name,weight,height)
print(a)
