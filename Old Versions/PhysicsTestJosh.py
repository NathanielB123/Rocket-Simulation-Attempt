import matplotlib.pyplot as plt
import math as m

RocketAngle = 60
RocketThrust = 50
EarthMass = (5.972 * 10 ** 24)
RocketMass = 1
RocketFuel = 0.5
RocketFuelUse = 0.1
T = 0
Acc = 0
Vel = 0
Dist = 0
Tchange = 0.0001
PrintInterval = 0
forceDueToFuel = (m.sin(m.radians(RocketAngle)) * 50)
tlist = [0]
ylist = [0]
y2list = [0]
y3list = [0]
y4list = [0]
ListOfAccs=[0]
while RocketFuel - RocketFuelUse * T > 0:
    TotalMass = RocketMass + (RocketFuel - RocketFuelUse*T)
    AccDueToG = 6.67408 * 10 ** -11 * EarthMass / ((Dist + 6371 * 1000) ** 2)
    Acc = forceDueToFuel / TotalMass - AccDueToG
    Vel += Acc * Tchange
    Dist += Vel * Tchange
    T += Tchange
    PrintInterval += 1
    tlist.append(T)
    ylist.append(Dist)
    y2list.append(Vel)
    y3list.append(Acc)
    y4list.append(Acc-ListOfAccs[-1])
    ListOfAccs.append(Acc)
y4list.pop(1)
tlist2=[]
for i in tlist:
    tlist2.append(i)
tlist2.pop(1)


    
print(Dist)

def plot():
    plt.figure(1)
    plt.plot(tlist,ylist) 
    plt.ylabel("Distance (m)") 
    plt.xlabel("Time (s)")
    plt.grid()

    plt.figure(2)
    plt.plot(tlist,y2list)
    plt.ylabel("Velocity (ms^-1)") 
    plt.xlabel("Time (s)")
    plt.grid()

    plt.figure(3)
    plt.plot(tlist,y3list)
    plt.ylabel("Acceleration (ms^-2)") 
    plt.xlabel("Time (s)")
    plt.grid()

    plt.figure(4)
    plt.plot(tlist2,y4list)
    plt.ylabel("Rate of acceleration (ms^-3)") 
    plt.xlabel("Time (s)")
    plt.grid()

    plt.show()


    
plot()
