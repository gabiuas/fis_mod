from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import arange
from math import *
from numpy import linspace





t=np.arange(0,4,0.001)
X1=[]
Y1=[]
A1=[]
X2=[]
Y2=[]
A2=[]




def pendulo(z,t):
	
	a=z[0]
	w=z[1]

	dadt=w
	dwdt=-(g*math.cos(a))/r
	

	return [dadt,dwdt]




#Parametros Angulo1
an=11.5
ang=radians(an-90)
g=9.8
m=2
r=2.28
w0=0
z0=[ang,w0]
S1=odeint(pendulo, z0, t)




#Parametros Angulo2
an=41.4
ang=radians(an-90)
g=9.8
m=2
r=2.28
w0=0
z0=[ang,w0]
S2=odeint(pendulo, z0, t)





for e in range(len(t)):

	x1=math.cos((S1[e,0]))*r
	X1.append(x1)

	y1=math.sin((S1[e,0]))*r
	Y1.append(y1)

	a1=(S1[e,0])*180/math.pi
	A1.append(a1)

	x2=math.cos((S2[e,0]))*r
	X2.append(x2)

	y2=math.sin((S2[e,0]))*r
	Y2.append(y2)

	a2=(S2[e,0])*180/math.pi
	A2.append(a2)




#Angulo1
plt.plot(X1,Y1)
plt.xlabel('X (em metros)')
plt.ylabel('Y (em metros)')
plt.title('Trajetória (ângulo 11,6º)')
plt.axis([-2.5,2.5,-2.5,2.5])
plt.grid(True)
plt.show()

plt.plot(t,X1)
plt.ylabel('X (em metros)')
plt.xlabel('Tempo (em segundos)')
plt.title('X por Tempo (ângulo 11,6º)')
plt.axis([0,3.4,-0.5,0.5])
plt.grid(True)
plt.show()

plt.plot(t,Y1)
plt.ylabel('Y (em metros)')
plt.xlabel('Tempo (em segundos)')
plt.title('Y por Tempo (ângulo 11,6º)')
plt.axis([0,3.4,-2.29,-2.23])
plt.grid(True)
plt.show()

plt.plot(t,A1)
plt.ylabel('Ângulo (em graus)')
plt.xlabel('Tempo (em segundos)')
plt.title('Ângulo por Tempo (ângulo 11,6º)')
plt.axis([0,3.4,-102,-78.3])
plt.grid(True)
plt.show()




#Angulo2
plt.plot(X2,Y2)
plt.xlabel('X (em metros)')
plt.ylabel('Y (em metros)')
plt.title('Trajetória (ângulo 41,4º)')
plt.axis([-2.5,2.5,-2.5,2.5])
plt.grid(True)
plt.show()

plt.plot(t,X2)
plt.ylabel('X (em metros)')
plt.xlabel('Tempo (em segundos)')
plt.title('X por Tempo (ângulo 41,4º)')
plt.axis([0,3.4,-1.55,1.55])
plt.grid(True)
plt.show()

plt.plot(t,Y2)
plt.ylabel('Y (em metros)')
plt.xlabel('Tempo (em segundos)')
plt.title('Y por Tempo (ângulo 41,4º)')
plt.axis([0,3.4,-2.29,-1.7])
plt.grid(True)
plt.show()


plt.plot(t,A2)
plt.ylabel('Ângulo (em graus)')
plt.xlabel('Tempo (em segundos)')
plt.title('Ângulo por Tempo (ângulo 41,4º)')
plt.axis([0,3.4,-135,-47,])
plt.grid(True)
plt.show()





	





