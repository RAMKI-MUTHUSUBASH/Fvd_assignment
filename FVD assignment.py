import matplotlib
from matplotlib import pyplot as plotting
from matplotlib import *
import math
from math import *


'''w=float(input("Enter the weight of the aircraft in N ="))
AR=float(input("Enter the Aspect Ratio ="))
s=float(input("Enter the wing area in m^2 ="))
h=float(input("Enter the Altitude of the aircraft flying ="))
Cd0=float(input("Enter the profile Drag of the aircraft ="))
e=float(input("Enter the value of e ="))
Ta0=float(input("Enter the Thrust available at sea level ="))'''
w=219540
AR=11
s=377
h=15240
Cd0=0.017
e=0.85
Ta0=2*285000

p0=1.225   #in kg/m^3 units
T0=288     #in K scale
l=0.0065
R=287      #in J/mol-K units
k=1/(pi*e*AR)
print(k)
v=30
Tr=[]
Pr=[]
V=[]
i=0
m=0.9
Clminr=0
a=0


if 0<h<=11000:
    T=T0-(l*h)
    p=p0*((T/T0)**((9.81/(R*l))-1))
    print("Density at given height ",h," = ",p)
    print("Temperature at given height ",h," =",T)
elif 11000<h<=25000:
    T=T0-(l*11000)
    p11000=p0*((T/T0)**((9.81/(R*l))-1))
    p=p11000*(e**((-9.81*(h-11000))/(R*T)))
    print("Density at given height ",h," = ",p)
    print("Temperature at given height ",h," =",T)

#minimum thrust calculation:
Cdmint=2*Cd0
Clmint=(Cd0/k)**0.5
Vmint=((2*w)/(p*s*Clmint))**0.5
Trmin=w*(Cdmint/Clmint)
print("For minimum velocity of ",Vmint," m/s","minimum Thrust is ",Trmin," Watts")

#minimum power calculation:
Cdminp=4*Cd0
Clminp=((3*Cd0)/k)**0.5
Vminp=(((2*w)/(p*s))**0.5)*((k/(2*Cd0))**0.25)
Prmin=w*(Cdminp/Clminp)*Vminp
print("For minimum velocity of ",Vminp," m/s","minimum Power is ",Prmin," Watts")

#Thrust Available calculation:
Ta=Ta0*((p/p0)**m )
print("Ta=",Ta," N")

# maximum velocity calculation:
a=(Ta/w)*(w/s)
b=(w/s)*((((Ta/w)**2)-(4*Cd0*k))**0.5)
c=p*Cd0
Vmax=((a+b)/c)**0.5
print("Vmax=",Vmax," m/s")

# maximum rate of climb:
Clminr1=(-(Ta/w)+((Ta/w)**2-(4*k*(-3*Cd0)))**0.5)/(2*k)
Clminr2=(-(Ta/w)-(((Ta/w)**2)-(4*k*(-3*Cd0)))**0.5)/(2*k)
if Clminr1>0:
    Clminr=Clminr1
elif Clminr2>0:
    Clminr=Clminr2
print(Clminr)
Cdminr=Cd0+(k*(Clminr**2))
print(Cdminr)
VClmin=((2*w)/(p*s*Clminr))**0.5
rc_max=((Ta/w)-(Cdminr/Clminr))*VClmin
print("max rate of climb=",rc_max," m/s")

#maximum angle of climb:
Clmina=(Cd0/k)**0.5
Cdmina=2*Cd0
x=(Ta/w)-(Cdmina/Clmina)
print(x)
a_max=asin(x)
a_max=(a_max*180)/pi
print("max angle of climb=",a_max," degree")




while v<=500:
    V.append(v)
    Cl=(2*w)/(p*(v**2)*s)
    Cd=Cd0+(k*(Cl**2))
    tr=w*(Cd/Cl)
    Tr.append(tr)
    pr=tr*v
    Pr.append(pr)
    v=v+10
    
while i<=47:
    print("V=",V[i]," m/s","\t","Tr=",Tr[i]," N","\t","Pr=",Pr[i]," Watts")
    i=i+1
    
while True:
    call=input(str())
    if call=="t":
        f1=plotting.plot(V,Tr,label="Thrust Vs Velocity Curve")
        f1=plotting.plot(Vmint,Trmin,"-bd",color="red",label="Thrust for Minimum Velocity")
        f1=plotting.plot(Vmax,Ta,"-bd",color="black",label="Thrust for Maximum Velocity")
        plotting.legend()          
        plotting.grid()
        plotting.title("Thrust Vs Velocity")
        plotting.xlabel("Velocity (m/s)")
        plotting.ylabel("Thrust Required (N)")
        plotting.show()
    elif call=="p":
        f2=plotting.plot(V,Pr,label="Power Vs Velocity Curve")
        f2=plotting.plot(Vminp,Prmin,"-bo",color="orange",label="Power for Minimum Velocity")
        plotting.legend()
        plotting.grid()
        plotting.title("Power Vs Velocity")
        plotting.xlabel("Velocity (m/s)")
        plotting.ylabel("Power Required (Watts)")
        plotting.show()
    elif call=="q":
        break

    
