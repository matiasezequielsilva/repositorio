num1=int(input("Agregue el primer numero:"))
num2=int(input("Agregue el segundo numero:"))
num3=int(input("Agregue el tercer numero:"))
print("El mayor es:")
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
    
