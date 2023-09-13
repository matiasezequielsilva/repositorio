#recorriendo todos los key-value pairs
fav_numbers = {'eric' : 17, 'ever' : 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))
# todos los keys
for name in fav_numbers.keys():
    print(name + ' loves a number')
# todos los values
for number in fav_numbers.values():
    print(str(number) + ' is a favorite number for someone')
