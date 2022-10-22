pesos=0
meses=1
anos=0
casa=int(input("Ingrese el valor de la casa:"))
casa=int(casa)
alquiler=float(input("Ingrese el alquiler:"))
alquiler=float(alquiler)
while pesos<=casa:
    if meses>=12:
        anos=anos+1
        print (meses)
        meses=0
        alquiler=alquiler*1.3
    pesos=pesos+alquiler
    meses=meses+1
print("Se llegara al valor de la casa en:" , anos , " años y " , meses , " meses")
#{:.0f} = Redondeo
print ("con $" , "{:.0f}".format(pesos) , "pesos")
print ("con un alquier de $" , "{:.0f}".format(alquiler) )
