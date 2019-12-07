import time
RocketAngle=60
RocketThrust=50
EarthMass=5.972*10**24
RocketMass=1
RocketFuel=0.5
RocketFuelUse=0.1
T=0
Acc=0
Vel=0
Dist=0
Tchange = 0.000001
PrintInterval=0
while RocketFuel-RocketFuelUse*T>0:
    TotalMass=1.5-0.1*T
    AccDueToG=6.67408*10**-11*(EarthMass)/((Dist+6371*1000)**2)
    Acc = 43/TotalMass - AccDueToG
    Vel += Acc*Tchange
    Dist += Vel*Tchange
    T+=Tchange
    PrintInterval+=1
    if round(PrintInterval/1000000)==PrintInterval/1000000:
        print("at T =", str(T), "\nM =",str(Dist))







    




