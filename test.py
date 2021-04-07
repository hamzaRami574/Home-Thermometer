temp = 25
print("Temperture is:") 
print(temp)
thermo = temp
print("thermo's Temperture is: ")
print(thermo)
print('Enter wanted Temperture:')
wantedtemp = int(input())
InCaseGreater = wantedtemp - temp
InCaseLesser = temp - wantedtemp
if wantedtemp > temp:
    thermo = thermo + InCaseGreater
    print("thermo's Temperture is:") 
    print(thermo)
elif wantedtemp < temp:
    thermo = thermo - InCaseLesser
    print("thermo's Temperture is:") 
    print(thermo)

else: 
    print("Temperture already set to:") 
    print(temp)

