'''
1D Advection equation by finite difference method(forward time forward difference)
@kaushik kalita 
Date : 22/09/2023

'''
import numpy as np
import matplotlib.pyplot as plt
import sys

#define simulation domain
L  = 2 
N  = int(input('enter the no of node points : ')) 
dx = L/(N-1) # lenght element
T  = int(input('enter total simulation time in seconds : ')) 
dt = float(input("enter the time step :"))
Nt = int(T/dt)

print("grid spacing is :",dx) 
print("time step is  :",dt) 
print("total time step is :",Nt)
print("value of dx/dt is :",dx/dt)

v  = float(input('input velocity : '))

k = v*(dt/dx)

print("value of alpha is ",k)

if((dx/dt)<v):
    print("dx/dt<v , CFL condition isnot satisfied" )
    print("exiting")
    sys.exit()

x = np.linspace(0,L,N)
u = np.zeros(N)

u1 = np.zeros(N)
u2 = np.zeros(N)
u3 = np.zeros(N)
u_int = np.zeros(N)

fig, ax = plt.subplots(1, 3, figsize=(10, 5))


#input function 
for i in range(N):
    if x[i]<0.5:
        u[i]=0
        continue
    if x[i]<=1.0 and x[i]>= 0.5:
        u[i]= 2*x[i]-1
        continue
    if x[i]>=1 and x[i]<=1.5:
        u[i] = 3 - 2*x[i]
        continue
    if x[i]>=1.5:
        u[i]=0
        u[0]=u[N-1]

"""
#input function

u[i] = np.sin((2*np.pi*i*dx)/L)
u[0]= 0
u[N-1] = 0


#input function
u = np.exp(-((x-1)**2))
u[0]= u[1]
u[N-1] = u[2]
"""

u_int = np.copy(u)

u1 = np.copy(u)
u2 = np.copy(u)
u3 = np.copy(u)

#for t in np.arange(0, T, dt):
for t in range(Nt+1):
    #FTFS(forward)
    u1[1:N-1] = u1[1:N-1] - k*(u1[2:N] - u1[1:N-1])

    ax[0].clear()
    ax[0].plot(x,u1,label="output function(FTFS)")
    #ax[0].plot(x,u_int,label="input finction")
    ax[0].set_xlabel("x")
    ax[0].set_ylabel("rho")
    ax[0].set_title('Time Step: {:.2f}'.format(t))
    ax[0].set_xlim([0,L])
    #ax[1].set_ylim([-10,10])
    ax[0].legend()

    #backward
    u2[1:N-1] = u2[1:N-1] - k*(u2[1:N-1] - u2[0:N-2])

    ax[1].clear()
    ax[1].plot(x,u2,label="output function (FTBS)")
    #ax[1].plot(x,u_int,label="input finction")
    ax[1].set_xlabel("x-vt")
    ax[1].set_ylabel("rho")
    ax[1].set_title('Time Step: {:.2f}'.format(t))
    ax[1].set_xlim([0,L])
    #ax[1].set_ylim([-10,10])
    ax[1].legend()


    #FTCS
    u3[1:N-1] = u3[1:N-1] - k*(u3[2:N] - u3[0:N-2]) 
    
    ax[2].clear()
    ax[2].plot(x,u3,label="output function(FTCS)")
    #ax[2].plot(x,u_int,label="input finction")
    ax[2].set_xlabel("x-vt")
    ax[2].set_ylabel("rho")
    ax[2].set_title('Time Step: {:.2f}'.format(t))
    ax[2].set_xlim([0,L])
    #ax[1].set_ylim([-10,10])
    ax[2].legend()

    plt.pause(1)
plt.show()








