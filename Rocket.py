import matplotlib.pyplot as plt
import math as m
from tkinter import *
import random

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Rocket Physics Simulation (Y)")
        
        self.inputbutton = Button(root, text= "Input", command = self.input).grid(row=13,column=6)
        self.clearbutton = Button(root, text="Clear", command= self.cleartext).grid(row = 14, column = 6)  
  
        self.RocketAngleText = Label(root, text= "Rocket Angle (degrees from up)").grid(row=5, column = 4)
        self.RocketAngle2Text = Label(root, text= "Rocket Angle 2 (degrees from up)").grid(row=7, column = 4)
        self.RocketThrustText = Label(root, text= "Rocket Thrust (N)").grid(row = 9, column = 4)
        self.masstext = Label(root, text= "Dry Rocket Mass (kg)").grid(row=11, column = 4)
        self.fueltext = Label(root, text= "Mass of Fuel (kg)").grid(row = 13, column = 4)
        self.fuelusetext = Label(root, text= "Fuel use (kgs^-1)").grid(row = 15, column = 4)

        self.RocketAngle = Entry()
        self.RocketAngle.grid(row = 5, column = 5)
        self.RocketAngle2 = Entry()
        self.RocketAngle2.grid(row = 7, column = 5)
        self.RocketThrust = Entry()
        self.RocketThrust.grid(row = 9, column = 5)
        self.Mass = Entry()
        self.Mass.grid(row = 11, column = 5)
        self.FuelMass = Entry()
        self.FuelMass.grid(row = 13, column = 5)
        self.FuelUse = Entry()
        self.FuelUse.grid(row = 15, column = 5)


        self.grid()
        

    def cleartext(self):
        self.RocketAngle.delete(0, 'end')
        self.RocketAngle2.delete(0, 'end')
        self.RocketThrust.delete(0, 'end')
        self.Mass.delete(0, 'end')
        self.FuelMass.delete(0, 'end')
        self.FuelUse.delete(0, 'end')

    def runsim(self, RocketAngle, RocketAngle2, RocketThrust, RocketMass, RocketFuel, RocketFuelUse):
        PlanetMass = 5.972*10**24 
        PlanetRadius = 6371*1000
        T = 0
        Acceleration=[0,0,0]
        Velocity=[0,0,0]
        Displacement=[0.01,PlanetRadius+10,0.01]
        TimeInterval = 0.001

        Thrust = [(m.sin(m.radians(RocketAngle)) * RocketThrust), #X
                  (m.cos(m.radians(RocketAngle)) * (m.cos(m.radians(RocketAngle2)) * RocketThrust)), #Y
                  (m.sin(m.radians(RocketAngle2)) * RocketThrust)] #Z
        tlist = [0]
        ylist = [0]
        y2list = [0]
        y3list = [0]
        x4list=[0]
        y4list=[0]

        while m.sqrt(Displacement[0]**2+Displacement[1]**2+Displacement[2]**2) >= PlanetRadius and T<1000:
            #print(m.sqrt(Displacement[0]**2+(Displacement[1]-PlanetRadius)**2+Displacement[2]**2))
            if RocketFuel - RocketFuelUse*T>0:
                TotalMass = RocketMass + (RocketFuel - RocketFuelUse*T)
            else:
                TotalMass = RocketMass
            AccDueToG = 6.67408 * 10 ** -11 * PlanetMass / ((m.sqrt(Displacement[0]**2+Displacement[1]**2+Displacement[2]**2)) ** 2) * -1
            AccDueToGAngle = m.degrees(m.atan(Displacement[1]/Displacement[0]))+90
            AccDueToGAngle2 = m.degrees(m.atan(Displacement[1]/Displacement[2]))+90
            if RocketFuel - RocketFuelUse*T>0:
                Acceleration[0] = (Thrust[0] / TotalMass) + AccDueToG * m.sin(m.radians(AccDueToGAngle))
                Acceleration[1] = (Thrust[1] / TotalMass) + AccDueToG * m.cos(m.radians(AccDueToGAngle)) * (m.cos(m.radians(AccDueToGAngle2)))
                Acceleration[2] = (Thrust[2] / TotalMass) + AccDueToG * m.sin(m.radians(AccDueToGAngle2))
            else:
                Acceleration[0] = AccDueToG * m.sin(m.radians(AccDueToGAngle))
                Acceleration[1] = AccDueToG * m.cos(m.radians(AccDueToGAngle)) * (m.cos(m.radians(AccDueToGAngle2)))
                Acceleration[2] = AccDueToG * m.sin(m.radians(AccDueToGAngle2))

            Velocity[0] += Acceleration[0] * TimeInterval
            Velocity[1] += Acceleration[1] * TimeInterval
            Velocity[2] += Acceleration[2] * TimeInterval
            Displacement[0] += Velocity[0] * TimeInterval
            Displacement[1] += Velocity[1] * TimeInterval
            Displacement[2] += Velocity[2] * TimeInterval
            T += TimeInterval

            tlist.append(T)
            #ylist.append(m.sqrt(Displacement[0]**2+(Displacement[1]-PlanetRadius)**2+Displacement[2]**2))
            #y2list.append(m.sqrt(Velocity[0]**2+Velocity[1]**2+Velocity[2]**2))
            #y3list.append(m.sqrt(Acceleration[0]**2+Acceleration[1]**2+Acceleration[2]**2))
            ylist.append(m.sqrt(Displacement[0]**2+Displacement[1]**2+Displacement[2]**2)-PlanetRadius)
            y2list.append(m.sqrt(Velocity[0]**2+Velocity[1]**2+Velocity[2]**2))
            y3list.append(m.sqrt(Acceleration[0]**2+Acceleration[1]**2+Acceleration[2]**2))
            y4list.append(Displacement[1]-PlanetRadius)
            x4list.append(Displacement[0])
        
        plt.figure(1)
        plt.plot(tlist,ylist) 

        plt.ylabel("Displacement (m)")
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
        plt.plot(x4list,y4list)
        plt.ylabel("Y (m)") 
        plt.xlabel("X (m)")
        plt.grid()
        print(x4list[1000])
        print(y4list[1000])

        plt.show()

        
    def input(self):
        RocketAngle = float(self.RocketAngle.get())
        RocketAngle2 = float(self.RocketAngle2.get())
        RocketThrust = float(self.RocketThrust.get())
        RocketMass = float(self.Mass.get())
        RocketFuel = float(self.FuelMass.get())
        RocketFuelUse = float(self.FuelUse.get())

        self.runsim(RocketAngle,RocketAngle2,RocketThrust, RocketMass, RocketFuel, RocketFuelUse)




root = Tk()
app = Window(root)
root.mainloop
